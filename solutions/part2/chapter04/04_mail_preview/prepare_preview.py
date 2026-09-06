"""메일 미리보기와 드라이런 로그 생성. 네트워크·로그인·발송 기능 없음."""
import argparse
from email.message import EmailMessage
from email.policy import SMTP
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--draft', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    draft = args.draft.read_text(encoding='utf-8')
    if '## 본문\n' not in draft:
        raise ValueError('초안에 ## 본문 제목이 없습니다.')
    body = draft.split('## 본문\n', 1)[1].strip()
    recipient = 'me@example.com'
    subject = '[본인 시험용 미리보기] 분기 안내 메일'
    message = EmailMessage(policy=SMTP)
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / 'preview.eml').write_bytes(message.as_bytes())
    (args.output / 'preview.md').write_text(
        f'# 시험 메일 미리보기\n\n받는 사람: {recipient} (실제 발송 전 본인이 직접 자기 주소로 교체)\n\n'
        f'참조·숨은 참조: 없음\n\n제목: {subject}\n\n첨부: 없음\n\n'
        f'## 본문\n\n{body}\n\n---\n\n아직 실제 발송하지 않았습니다.\n', encoding='utf-8')
    log = {'mode': 'dry-run', 'recipient': recipient, 'cc': [], 'bcc': [],
           'attachments': [], 'sent': False, 'approval': '미확인',
           'note': '가상 주소 미리보기 파일만 생성. 실제 시험은 사용자가 메일 서비스에서 직접 수행.'}
    (args.output / 'dry_run.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('미리보기 2개와 드라이런 로그 1개 생성. 실제 발송 0건.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(f'중단: {error}')
