"""가상 example.com 거래처의 Markdown 초안만 만듭니다. 발송 기능이 없습니다."""
import argparse
import csv
from pathlib import Path
import re

FIELDS = ['회사명', '담당자명', '직함', '메일주소']


def read_recipients(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError('열 이름과 순서가 회사명, 담당자명, 직함, 메일주소인지 확인하세요.')
        rows = list(reader)
    if not rows:
        raise ValueError('거래처가 없습니다.')
    addresses = set()
    for number, row in enumerate(rows, 1):
        if any(not row.get(field, '').strip() for field in FIELDS[:3]):
            raise ValueError(f'{number}행 필수 값 누락: 목록을 고친 뒤 다시 실행하세요.')
        if row['직함'] not in {'님', '사장님', '대표님'}:
            raise ValueError(f'{number}행 직함을 확인하세요.')
        address = row['메일주소']
        if address and not re.fullmatch(r'[A-Za-z0-9._+-]+@example\.com', address, re.I):
            raise ValueError('이 연습은 example.com 가상 주소만 사용합니다.')
        if address and address.casefold() in addresses:
            raise ValueError(f'{number}행 수신자 중복입니다.')
        if any('\n' in value or '\r' in value for value in row.values()):
            raise ValueError('필드 안의 줄바꿈은 허용하지 않습니다.')
        if address:
            addresses.add(address.casefold())
    return rows


def render(row):
    name = row['담당자명']
    salutation = name + '님' if row['직함'] == '님' else name + ' ' + row['직함']
    return f'''# 거래처 안내 메일 초안

- 수신자: {row['메일주소'] or '[확인 필요]'}
- 제목: [검토용 초안] 2026년 3분기 협업 결과와 다음 일정 안내
- 첨부 파일: [확인 필요]
- 회신 마감일: [확인 필요]
- 최종 승인자: [확인 필요]
- 상태: 파일로만 저장, 발송하지 않음

## 본문

{row['회사명']} {salutation}, 안녕하세요.

연습출판 기획팀입니다. 2026년 3분기 함께 진행한 내용을 안내드립니다.
이번 분기에는 공동 자료집 2종을 제작하고 온라인 설명회 1회를 운영했습니다.

다음 분기에는 2026년 10월 7일 자료집 개정안을 공유할 예정입니다.
관련 내용을 확인해 주시고 수정할 사항이 있으면 알려 주세요.
회신 마감일은 [확인 필요]이며 첨부 파일도 [확인 필요]입니다.

협업해 주셔서 감사합니다.
연습출판 기획팀 드림

※ 이 내용은 교육용 가상 자료를 바탕으로 만든 초안입니다.
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recipients', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--limit', type=int)
    args = parser.parse_args()
    rows = read_recipients(args.recipients)
    if args.limit is not None and not 1 <= args.limit <= len(rows):
        parser.error('--limit은 1부터 전체 거래처 수까지여야 합니다.')
    selected = rows[:args.limit] if args.limit else rows
    args.output.mkdir(parents=True, exist_ok=False)
    for number, row in enumerate(selected, 1):
        (args.output / f'draft_{number:03d}.md').write_text(render(row), encoding='utf-8')
    print(f'목록 {len(rows)}개 확인, 초안 {len(selected)}개 저장, 실제 발송 0건.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(f'중단: {error}')
