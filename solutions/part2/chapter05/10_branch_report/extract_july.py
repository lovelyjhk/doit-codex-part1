"""Stream the CSV without retaining the source or previous chunks in memory.

This calculation stage creates selected.csv, summary.json and chunk-log.txt.
It deliberately stops on bad source fields. It never overwrites output files.
"""
from pathlib import Path
from itertools import islice
from datetime import date
import argparse
import csv
import json
import hashlib

REGIONS = ['광주', '대전', '부산', '서울']
FIELDS = ['date', 'region', 'category', 'sales', 'quantity']

def extract(source, output, chunk_size=200):
    source, output = Path(source), Path(output)
    if chunk_size < 1:
        raise ValueError('묶음 크기는 1 이상이어야 합니다.')
    names = ['selected.csv', 'summary.json', 'chunk-log.txt']
    if any((output/name).exists() for name in names):
        raise FileExistsError('기존 결과를 보존합니다. 다른 출력 폴더를 지정하세요.')
    output.mkdir(parents=True, exist_ok=True)
    total = selected = sales = quantity = 0
    regions = {name: {'count': 0, 'sales': None, 'quantity': None} for name in REGIONS}
    first = last = None
    chunk_count = 0
    with source.open(encoding='utf-8-sig', newline='') as stream, (output/'selected.csv').open('x', encoding='utf-8-sig', newline='') as extracted, (output/'chunk-log.txt').open('x', encoding='utf-8') as log:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError(f'열 이름 확인 필요: {reader.fieldnames}')
        writer = csv.DictWriter(extracted, fieldnames=FIELDS)
        writer.writeheader()
        log.write(f'원본: {source.name}\n기간: 2026-07-01 이상, 2026-08-01 미만\n묶음 크기: {chunk_size}행\n')
        while True:
            chunk = list(islice(reader, chunk_size))
            if not chunk:
                break
            chunk_count += 1
            picked = chunk_sales = chunk_quantity = 0
            for row in chunk:
                total += 1
                try:
                    if set(row) != set(FIELDS) or any(v is None or not v.strip() for v in row.values()):
                        raise ValueError('빈 값 또는 열 수 불일치')
                    day = date.fromisoformat(row['date'])
                    amount, units = int(row['sales']), int(row['quantity'])
                    if row['region'] not in regions:
                        raise ValueError('요청 범위 밖 지역')
                except (ValueError, TypeError) as exc:
                    message = f'데이터 {total}행(머리글 제외) 확인 필요: {exc}. 임의 수정·제외하지 않고 중단했습니다.'
                    log.write(message+'\n')
                    raise ValueError(message) from exc
                if date(2026, 7, 1) <= day < date(2026, 8, 1):
                    writer.writerow(row)
                    picked += 1; selected += 1
                    chunk_sales += amount; sales += amount
                    chunk_quantity += units; quantity += units
                    group = regions[row['region']]
                    group['count'] += 1
                    group['sales'] = (group['sales'] or 0) + amount
                    group['quantity'] = (group['quantity'] or 0) + units
                    first = day if first is None else min(first, day)
                    last = day if last is None else max(last, day)
            log.write(f'묶음 {chunk_count}: 처리 {len(chunk)}행, 선택 {picked}행, 제외 {len(chunk)-picked}행, 선택 매출 {chunk_sales:,}원, 수량 {chunk_quantity:,}개 | 누적 처리 {total}행, 선택 {selected}행, 제외 {total-selected}행, 매출 {sales:,}원, 수량 {quantity:,}개\n')
        log.write(f'전체: {chunk_count}묶음, 처리 {total}행, 선택 {selected}행, 제외 {total-selected}행, 매출 {sales:,}원, 수량 {quantity:,}개\n')
    result = dict(source=source.name,period_start='2026-07-01',period_end_exclusive='2026-08-01',chunk_size=chunk_size,chunk_count=chunk_count,processed=total,selected=selected,excluded=total-selected,sales=sales,quantity=quantity,first_date=str(first) if first else None,last_date=str(last) if last else None,regions=regions)
    (output/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='가상 CSV에서 2026년 7월 기록을 나누어 읽고 추출합니다.')
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--chunk-size', type=int, default=200)
    args=parser.parse_args()
    print(json.dumps(extract(args.source,args.output,args.chunk_size),ensure_ascii=True))
