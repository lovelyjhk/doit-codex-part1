"""30분 간격·하루 3회·명시 승인·로컬 이상 로그를 연습합니다. 메일은 보내지 않습니다."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path


def check_allowed(state, now):
    history = [datetime.fromisoformat(value) for value in state.get('runs', [])]
    if history and (now - max(history)).total_seconds() < 30 * 60:
        raise ValueError('마지막 실행 후 30분이 지나지 않았습니다.')
    if sum(value.date() == now.date() for value in history) >= 3:
        raise ValueError('오늘 최대 3회에 도달했습니다.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', type=Path, required=True)
    parser.add_argument('--confirm', choices=['RUN'])
    args = parser.parse_args()
    if args.confirm != 'RUN':
        print('미리보기: 승인 시 현재 시각을 로컬 상태 파일에 기록합니다. 메일 발송은 없습니다.')
        return
    args.state.parent.mkdir(parents=True, exist_ok=True)
    lock = args.state.with_suffix('.lock')
    try:
        handle = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise SystemExit('다른 실행이 진행 중이거나 중단 기록이 있습니다. 실행 상태를 먼저 확인하세요.')
    try:
        os.close(handle)
        now = datetime.now().astimezone()
        state = json.loads(args.state.read_text(encoding='utf-8')) if args.state.exists() else {'runs': []}
        try:
            check_allowed(state, now)
        except ValueError as error:
            alert = args.state.with_name('local_alerts.jsonl')
            with alert.open('a', encoding='utf-8') as stream:
                stream.write(json.dumps({'time': now.isoformat(), 'reason': str(error), 'sent': False}, ensure_ascii=False) + '\n')
            raise
        state['runs'].append(now.isoformat())
        temporary = args.state.with_suffix('.pending')
        temporary.write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')
        temporary.replace(args.state)
        print('연습 실행 1회 기록. 실제 작업·메일 발송 없음.')
    finally:
        lock.unlink()


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, TypeError) as error:
        raise SystemExit(f'중단: {error}')
