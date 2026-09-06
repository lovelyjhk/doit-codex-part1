# 4장 파일·반복 업무 자동화

출판 준비용 초안입니다. 파일 이름 변경, 폴더 분류, 메일 초안, 회의록 스킬을 작은 가상 자료로 연습합니다. **미리 보기 → 검토 → 적용** 순서로 진행하세요.

## 실습 순서

| 절 | 실습 | 시작 자료 | 모범 답안 |
|---|---|---|---|
| 04-1 | [파일 이름 한 번에 바꾸기](01_rename_photos/README.md) | [start](01_rename_photos/start/) | [답안](../solutions/part2/chapter04/01_rename_photos/README.md) |
| 04-1 | [다운로드 폴더를 종류별로 나누기](02_sort_downloads/README.md) | [start](02_sort_downloads/start/) | [답안](../solutions/part2/chapter04/02_sort_downloads/README.md) |
| 04-2 | [거래처에 보낼 안내 메일 초안 만들기](03_mail_drafts/README.md) | [start](03_mail_drafts/start/) | [답안](../solutions/part2/chapter04/03_mail_drafts/README.md) |
| 04-2 | [작성한 메일의 발송 전 미리보기 준비하기](04_mail_preview/README.md) | [start](04_mail_preview/start/) | [답안](../solutions/part2/chapter04/04_mail_preview/README.md) |
| 04-3 | [회의록 정리 절차를 SKILL.md 한 장으로 저장하기](05_create_skill/README.md) | [start](05_create_skill/start/) | [답안](../solutions/part2/chapter04/05_create_skill/README.md) |
| 04-3 | [저장한 스킬을 다음 회의록에 그대로 써 보기](06_reuse_skill/README.md) | [start](06_reuse_skill/start/) | [답안](../solutions/part2/chapter04/06_reuse_skill/README.md) |

## 시작하기

1. 저장소를 내려받아 압축을 풀고 VS Code의 [파일] → [폴더 열기]로 `doit-codex-part1` 폴더를 엽니다.
2. 각 안내에서 지정한 `start` 폴더를 **새 `work` 하위 폴더에 복사**합니다. 이미 작업한 폴더에 덮어 복사하지 마세요. 책의 ‘연습용 폴더’가 이 복사본입니다.
3. VS Code에서 [터미널] → [새 터미널]을 엽니다. 아래 명령은 모두 **저장소 최상위 폴더**에서 Windows PowerShell로 실행합니다.
4. 코드 답안을 실행하려면 Python 3.10 이상이 필요합니다. `python --version`으로 확인합니다. 현재 PNG 이름 변경 실습은 기본 패키지만 사용합니다. 보충 EXIF JPG 예시에는 `python -m pip install Pillow`가 필요합니다. 명령이 동작하지 않으면 Python 설치 경로와 터미널을 먼저 확인하세요.
5. 프롬프트에서는 `이 폴더` 대신 `work/ch04-01/png`처럼 정확한 복사본 경로를 적습니다. `@` 뒤에 파일명을 입력했다면 제안 목록에서 해당 파일을 선택합니다.

`start`는 입력 자료, `prompts.md`는 복사할 요청문, `solutions`는 완료 예제입니다. 답안 코드를 그대로 실행하는 경로도 각 실습에 적었습니다. 먼저 직접 요청해 본 뒤 답안과 비교하세요.

[프롬프트 모음](PROMPTS.md) · [마무리 문제 3개](problems.md) · [모범 답안 전체](../solutions/part2/chapter04/README.md)

샘플의 회사·사람·실적·일정은 모두 가상입니다. 이름 변경용 PNG는 Twemoji 원본이며 출처와 CC BY 4.0 라이선스는 `chapter04/01_rename_photos/start/png/image_sources.txt`에 기록했습니다. 보충 JPG는 가상 EXIF 이미지입니다. 메일 코드는 파일 생성만 하며 네트워크에 연결하거나 발송하지 않습니다.
