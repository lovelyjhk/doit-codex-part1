import argparse
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager, ticker


def create_charts(input_path, output_dir, font_path):
    output_dir.mkdir(parents=True, exist_ok=True)
    targets = [output_dir / f"chart_{i:02d}.png" for i in range(1, 4)]
    if any(path.exists() for path in targets):
        raise FileExistsError("결과 PNG가 이미 있습니다. 다른 --output 폴더를 지정하세요.")
    if not font_path.is_file():
        raise FileNotFoundError("한글 폰트를 찾지 못했습니다. --font로 폰트 파일 경로를 지정하세요.")
    font_manager.fontManager.addfont(str(font_path))
    plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(font_path)).get_name()
    plt.rcParams["axes.unicode_minus"] = False
    monthly, categories, regions = defaultdict(int), defaultdict(int), defaultdict(int)
    with input_path.open(encoding="utf-8-sig", newline="") as stream:
        data = list(csv.DictReader(stream))
    for n, row in enumerate(data, 1):
        if any(not row.get(k) for k in ["month", "category", "region", "sales"]):
            raise ValueError(f"데이터 {n}행에 빈 값이 있습니다. 처리 기준을 먼저 정하세요.")
        value = int(row["sales"])
        monthly[row["month"]] += value
        categories[row["category"]] += value
        regions[row["region"]] += value
    total = sum(monthly.values())
    if total <= 0 or any(v < 0 for v in categories.values()):
        raise ValueError("도넛 그래프에 사용할 매출은 음수가 없고 합계가 양수여야 합니다.")
    palette = ["#235ca8", "#168572", "#c68722"]
    note = f"원본: {input_path.name} | 학습용 가상 데이터 | 원본 {len(data)}행 모두 합산"
    def frame(title):
        fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
        fig.patch.set_facecolor("white")
        ax.set_title(title, fontsize=22, loc="left", pad=24, color="#17365d")
        fig.subplots_adjust(left=.12, right=.93, top=.82, bottom=.20)
        fig.text(.12, .08, note, fontsize=11, color="#475569")
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        return fig, ax
    fig, ax = frame("2026년 월별 매출 추이")
    months = sorted(monthly)
    ax.plot(range(1, len(months)+1), [monthly[m] for m in months], color=palette[0], marker="o", linewidth=2.5)
    ax.set_xticks(range(1, len(months)+1), [f"{int(m[-2:])}월" for m in months])
    ax.set_xlabel("월", fontsize=13); ax.set_ylabel("매출(원)", fontsize=13)
    ax.set_ylim(0, 110000); ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
    ax.grid(axis="y", color="#e2e8f0"); ax.set_axisbelow(True)
    fig.text(.12, .125, "기간: 2026년 1~12월 / 집계: 월별 매출 합계(누적 아님)", fontsize=11)
    fig.savefig(targets[0], dpi=100); plt.close(fig)
    fig, ax = frame("2026년 카테고리별 매출 구성")
    labels = list(categories)
    ax.pie([categories[k] for k in labels], colors=palette, startangle=90,
           wedgeprops={"width":.42,"edgecolor":"white"}, autopct="%.1f%%", pctdistance=.78,
           textprops={"fontsize":14,"color":"white"})
    ax.text(0, .08, "전체 매출(원)", ha="center", fontsize=14)
    ax.text(0, -.16, f"{total:,}", ha="center", fontsize=21, weight="bold", color="#17365d")
    ax.legend([f"{k}: {categories[k]:,}원" for k in labels], loc="center left", bbox_to_anchor=(1.02,.5), frameon=False, fontsize=12)
    ax.set_position([.10,.20,.58,.60])
    fig.text(.12, .125, "기간: 2026년 1~12월 / 비율: 카테고리 매출 ÷ 전체 매출 / 도넛은 축 없음", fontsize=11)
    fig.savefig(targets[1], dpi=100); plt.close(fig)
    fig, ax = frame("2026년 지역별 매출 비교")
    labels = sorted(regions, key=regions.get, reverse=True)
    bars = ax.barh(labels, [regions[k] for k in labels], color=palette[0], height=.55)
    ax.invert_yaxis(); ax.set_xlabel("매출(원)", fontsize=13); ax.set_ylabel("지역", fontsize=13)
    ax.set_xlim(0, max(regions.values())*1.28)
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
    ax.bar_label(bars, labels=[f"{regions[k]:,}원" for k in labels], padding=8, fontsize=12)
    ax.grid(axis="x",color="#e2e8f0");ax.set_axisbelow(True)
    fig.text(.12, .125, "기간: 2026년 1~12월 / 집계: 지역별 매출 합계 / 매출축 0부터 시작", fontsize=11)
    fig.savefig(targets[2], dpi=100); plt.close(fig)
    print(f"PNG 3장 생성: 1200x800 픽셀, 매출 합계 {total:,}원")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("charts"))
    parser.add_argument("--font", type=Path, default=Path("C:/Windows/Fonts/malgun.ttf"))
    args = parser.parse_args()
    create_charts(args.input, args.output, args.font)
