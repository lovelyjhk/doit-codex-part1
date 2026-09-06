"""작은 연습 폴더용 변경 계획, 승인 적용, 복구. Python 3.10 이상."""
import argparse
from collections import Counter
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import sys

PNG_NAMES = {'1f600.png', '1f603.png', '1f604.png', '1f60a.png', '1f680.png'}


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(65536), b''):
            value.update(block)
    return value.hexdigest()


def is_link(path):
    info = path.lstat()
    return path.is_symlink() or bool(getattr(info, 'st_file_attributes', 0) & 1024)


def inside(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or rel.drive or '..' in rel.parts or not rel.parts:
        raise ValueError('계획에 폴더 밖 경로가 있습니다.')
    target = root / rel
    if not target.resolve().is_relative_to(root) or target.resolve() == root:
        raise ValueError('대상이 지정한 폴더 안의 파일이 아닙니다.')
    probe = root
    for part in rel.parts:
        probe = probe / part
        if probe.exists() and is_link(probe):
            raise ValueError('연결된 파일이나 폴더는 처리하지 않습니다.')
    return target


def record_path(root, path):
    result = path.resolve()
    if result.is_relative_to(root):
        raise ValueError('계획과 복구 기록은 처리 대상 폴더 밖에 저장하세요.')
    return result


def save_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def photo_date(path):
    from PIL import Image
    with Image.open(path) as image:
        exif = image.getexif()
        value = exif.get_ifd(34665).get(36867) or exif.get(36867)
    if not value:
        raise ValueError('EXIF 촬영일 없음')
    return datetime.strptime(str(value), '%Y:%m:%d %H:%M:%S').date()


def plan(root, kind, today):
    if kind == 'png':
        missing = sorted(name for name in PNG_NAMES if not (root / name).is_file())
        if missing:
            raise ValueError('지정한 PNG 파일이 없습니다: ' + ', '.join(missing))
    try:
        cutoff = today.replace(year=today.year - 1)
    except ValueError:
        cutoff = today.replace(year=today.year - 1, day=28)
    rows = []
    counters = Counter()
    for path in sorted(root.iterdir(), key=lambda item: item.name.casefold()):
        if is_link(path):
            rows.append({'old': path.name, 'new': '', 'action': 'hold', 'reason': '연결된 파일·폴더'})
            continue
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        if kind == 'png' and path.name not in PNG_NAMES:
            continue
        if kind == 'photos' and ext != '.jpg':
            continue
        if kind == 'simple' and not (path.name.startswith('IMG_') and ext == '.txt'):
            continue
        row = {'old': path.name, 'new': '', 'action': 'hold', 'reason': ''}
        if kind in ('sort', 'category') and (ext == '.tmp' or path.name.startswith('~$')):
            row['reason'] = '삭제 후보: 임시 파일, 그대로 보류'
            rows.append(row)
            continue
        if kind == 'png':
            with path.open('rb') as stream:
                if stream.read(8) != b'\x89PNG\r\n\x1a\n':
                    raise ValueError(f'PNG 형식을 확인할 수 없습니다: {path.name}')
            counters['all'] += 1
            new = f'photo_{today:%Y%m%d}_{counters["all"]:03d}.png'
            row['reason'] = f'한국 실행일 {today.isoformat()}; EXIF 미사용'
        elif kind == 'photos':
            try:
                day = photo_date(path)
            except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
                row['reason'] = f'확인 필요: {error}'
                rows.append(row)
                continue
            counters[day] += 1
            new = f'photo_{day:%Y%m%d}_{counters[day]:03d}.jpg'
            row['reason'] = f'EXIF 촬영일 {day.isoformat()}'
        elif kind == 'simple':
            counters['all'] += 1
            new = f'memo_{counters["all"]:03d}.txt'
            row['reason'] = 'IMG_ 텍스트 파일 이름순'
        elif kind == 'category':
            folder = '사진메모' if path.name.startswith('IMG_') and ext == '.txt' else '회의' if path.name.startswith('회의메모') and ext == '.txt' else '기타'
            new = (Path(folder) / path.name).as_posix()
            row['reason'] = '파일명 분류'
        else:
            modified = datetime.fromtimestamp(path.stat().st_mtime).date()
            row['modified'] = modified.isoformat()
            if modified <= cutoff:
                folder = '_archive'
                row['reason'] = f'1년 이상: {cutoff.isoformat()}까지'
            else:
                folder = {'.pdf': 'pdf', '.docx': 'docx', '.xlsx': 'xlsx'}.get(ext)
                folder = folder or ('이미지' if ext in {'.jpg', '.jpeg', '.png', '.gif', '.webp'} else '기타')
                row['reason'] = '파일 종류'
            new = (Path(folder) / path.name).as_posix()
        row['new'] = new
        target = inside(root, new)
        if target.exists():
            row['reason'] = '확인 필요: 대상 이름이 이미 있음'
        else:
            row['action'] = 'move'
            row['sha256'] = digest(path)
        rows.append(row)
    return {'version': 1, 'root': str(root), 'kind': kind, 'today': today.isoformat(), 'rows': rows}


def table(rows):
    print('| 기존 경로 | 새 경로 | 처리 | 이유 |')
    print('|---|---|---|---|')
    for row in rows:
        print(f'| {row["old"]} | {row["new"] or "그대로"} | {row["action"]} | {row.get("reason", "복구")} |')
    count = sum(row['action'] == 'move' for row in rows)
    print(f'이동 {count}개, 보류 {len(rows) - count}개. 삭제 0개.')


def validate_moves(root, rows):
    seen = set()
    for row in rows:
        src, dst = inside(root, row['old']), inside(root, row['new'])
        if not src.is_file() or digest(src) != row['sha256']:
            raise ValueError(f'원본 내용이 없거나 달라졌습니다: {row["old"]}')
        key = str(dst).casefold()
        if dst.exists() or key in seen:
            raise ValueError(f'대상 이름 충돌: {row["new"]}')
        seen.add(key)


def move_no_replace(src, dst):
    """xb로 기존 대상을 덮어쓰지 않고 복사한 뒤 원본 경로를 제거합니다."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with src.open('rb') as source, dst.open('xb') as target:
            created = True
            shutil.copyfileobj(source, target)
        shutil.copystat(src, dst)
        if digest(src) != digest(dst):
            raise ValueError('복사 내용이 일치하지 않아 중단합니다.')
        src.unlink()
    except Exception:
        if created and dst.exists():
            dst.unlink()
        raise


def apply_moves(root, rows, receipt_path):
    validate_moves(root, rows)
    receipt = {'version': 1, 'root': str(root), 'moves': [], 'complete': False}
    save_new(receipt_path, receipt)
    # 각 이동을 미리 기록하므로 중간에 종료되어도 복구 대상을 추적할 수 있습니다.
    for row in rows:
        receipt['moves'].append(row)
        receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        move_no_replace(inside(root, row['old']), inside(root, row['new']))
    receipt['complete'] = True
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(rows)}개 이동 완료. 복구 기록: {receipt_path.name}')


def undo_rows(root, receipt):
    rows = []
    for move in reversed(receipt['moves']):
        old, new = inside(root, move['old']), inside(root, move['new'])
        # 기록만 남기고 이동하기 전에 중단된 경우에는 복구할 필요가 없습니다.
        if old.is_file() and not new.exists() and digest(old) == move['sha256']:
            continue
        rows.append({'old': move['new'], 'new': move['old'], 'action': 'move', 'sha256': move['sha256']})
    validate_moves(root, rows)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('plan', 'apply', 'undo'):
        part = sub.add_parser(command)
        part.add_argument('--root', type=Path, required=True)
        if command == 'plan':
            part.add_argument('kind', choices=['png', 'photos', 'sort', 'category', 'simple'])
            part.add_argument('--today', type=date.fromisoformat, default=datetime.now(timezone(timedelta(hours=9))).date())
        if command in ('plan', 'apply'):
            part.add_argument('--plan', type=Path, required=True)
        if command in ('apply', 'undo'):
            part.add_argument('--receipt', type=Path, required=True)
            part.add_argument('--confirm')
    args = parser.parse_args()
    raw_root = args.root.absolute()
    if not raw_root.is_dir() or is_link(raw_root):
        raise ValueError('일반 연습 폴더를 지정하세요.')
    root = raw_root.resolve(strict=True)
    if args.command == 'plan':
        data = plan(root, args.kind, args.today)
        print(f'작업 폴더: {root}')
        table(data['rows'])
        save_new(record_path(root, args.plan), data)
        return
    record = record_path(root, args.plan if args.command == 'apply' else args.receipt)
    data = json.loads(record.read_text(encoding='utf-8'))
    if data.get('version') != 1 or Path(data['root']).resolve() != root:
        raise ValueError('이 기록은 지정한 연습 폴더의 기록이 아닙니다.')
    if args.command == 'apply':
        rows = [row for row in data['rows'] if row['action'] == 'move']
        table(data['rows'])
        if args.confirm != 'APPLY':
            raise ValueError('표를 검토한 뒤 --confirm APPLY를 지정하세요.')
        apply_moves(root, rows, record_path(root, args.receipt))
        print(f'성공 {len(rows)}개, 건너뜀 {len(data["rows"]) - len(rows)}개, 실패 0개.')
        for row in rows:
            print(f'최종 파일: {row["new"]}')
    else:
        rows = undo_rows(root, data)
        table(rows)
        if args.confirm != 'UNDO':
            print('복구 미리 보기입니다. 적용하려면 --confirm UNDO를 붙이세요.')
            return
        for row in rows:
            move_no_replace(inside(root, row['old']), inside(root, row['new']))
        print(f'{len(rows)}개 복구 완료. 빈 분류 폴더는 그대로 둡니다.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, ImportError, json.JSONDecodeError) as error:
        print(f'중단: {error}', file=sys.stderr)
        sys.exit(1)
