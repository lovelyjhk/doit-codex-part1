"""복사본의 샘플 수정일만 지정합니다. 원본 내용은 수정하지 않습니다."""
import argparse
from datetime import datetime
from pathlib import Path
import os

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--root', type=Path, required=True)
p.add_argument('--confirm', choices=['APPLY'])
args = p.parse_args()
root = args.root.resolve(strict=True)
names = {
    '안내.pdf': '2026-08-20', '분류연습_회의록.docx': '2026-08-20',
    '매출.xlsx': '2026-08-20', '이미지.jpg': '2026-08-20',
    '메모.txt': '2026-08-20', '오래된_기록.txt': '2025-08-01',
    '경계일_자료.txt': '2025-09-05', '작업중.tmp': '2025-08-01',
    '~$잠금파일.txt': '2026-08-20',
}
for name, day in names.items():
    path = root / name
    if not path.is_file() or path.is_symlink() or path.resolve().parent != root:
        raise SystemExit(f'정상 샘플 파일이 아닙니다: {name}')
    print(f'{name}: {day}')
if args.confirm != 'APPLY':
    print('미리 보기입니다. 적용하려면 --confirm APPLY를 붙이세요.')
else:
    for name, day in names.items():
        path = root / name
        timestamp = datetime.fromisoformat(day + 'T12:00:00').timestamp()
        os.utime(path, (path.stat().st_atime, timestamp))
    print('샘플 9개의 수정일을 설정했습니다.')
