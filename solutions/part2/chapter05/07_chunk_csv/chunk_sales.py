import argparse
import csv
import json
from itertools import islice
from pathlib import Path


def summarize(path, chunk_size):
    if chunk_size < 1:
        raise ValueError("청크 크기는 1 이상이어야 합니다.")
    result = {"row_count": 0, "chunk_count": 0, "sales_total": 0,
              "quantity_total": 0, "sales_by_region": {}}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"order_id", "date", "region", "sales", "quantity"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("필수 열이 없습니다.")
        while True:
            chunk = list(islice(reader, chunk_size))
            if not chunk:
                break
            result["chunk_count"] += 1
            for row in chunk:
                row_number = result["row_count"] + 1
                if any(not row.get(key) for key in required):
                    raise ValueError(f"데이터 {row_number}행에 빈 값이 있습니다.")
                try:
                    sales, quantity = int(row["sales"]), int(row["quantity"])
                except (ValueError, TypeError) as error:
                    raise ValueError(f"데이터 {row_number}행 숫자 형식 오류") from error
                result["row_count"] += 1
                result["sales_total"] += sales
                result["quantity_total"] += quantity
                region = row["region"]
                result["sales_by_region"][region] = result["sales_by_region"].get(region, 0) + sales
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV를 일정한 행 수로 나누어 합산합니다.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--chunk-size", type=int, default=200)
    parser.add_argument("--output", type=Path, default=Path("chunk_summary.json"))
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error("원본 CSV와 결과 경로가 같습니다.")
    if args.output.exists():
        parser.error("결과 파일이 이미 있습니다. 다른 --output 이름을 지정하세요.")
    answer = summarize(args.input, args.chunk_size)
    text = json.dumps(answer, ensure_ascii=False, indent=2)
    args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
