import argparse
import csv
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="학습용 CSV를 스트리밍 방식으로 생성합니다.")
    parser.add_argument("--rows", type=int, default=240000)
    parser.add_argument("--output", type=Path, default=Path("large_sales_generated.csv"))
    args = parser.parse_args()
    if args.rows < 1:
        parser.error("행 수는 1 이상이어야 합니다.")
    if args.output.exists():
        parser.error("같은 이름의 파일이 있습니다. 다른 출력 이름을 지정하세요.")
    with args.output.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["order_id", "date", "region", "sales", "quantity"])
        for i in range(args.rows):
            writer.writerow([f"L{i+1:06d}", f"2026-{i%12+1:02d}-{i%28+1:02d}",
                             ["서울", "부산", "대전", "광주"][i%4], (i%100+1)*100, i%5+1])
    groups, tail = divmod(args.rows, 100)
    expected = groups * 505000 + tail * (tail + 1) // 2 * 100
    print(f"생성 행 수: {args.rows:,}, 예상 매출 합계: {expected:,}원")
