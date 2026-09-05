import csv
from pathlib import Path


def main():
    csv_path = Path(__file__).with_name("sales_2026.csv")
    total = 0
    missing = 0

    with csv_path.open(encoding="utf-8-sig", newline="") as source:
        for row in csv.DictReader(source):
            amount = row["amount"].strip()
            if not amount:
                missing += 1
                continue
            total += int(amount)

    print(f"확인된 금액 합계: {total:,}원")
    print(f"누락된 금액: {missing}건")


if __name__ == "__main__":
    main()
