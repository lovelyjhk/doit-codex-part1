# 실습별 폴더 준비

파일 탐색기에서 문서 폴더 아래 `doit-work`를 만들고, 아래 이름으로 하위 폴더를 만듭니다. `doit-work`는 내려받은 저장소 폴더와 나란히 둡니다. 폴더마다 입력 자료가 다르므로 VS Code에서는 표에 적힌 **개별 폴더**를 엽니다.

## 첫째마당

[첫째마당 작업 규칙](../part1/RULES.md)을 먼저 읽고 1~2장에 해당하는 폴더만 준비합니다.

| 실습 | VS Code에서 열 폴더 | 복사할 파일 |
|---|---|---|
| 1장 본문 예시·마무리 문제 1 | `doit-work/01-prompts` | [예시 폴더](../chapter01/examples/README.md)의 report.md, document.md, meeting.md, sales_2026.csv |
| 1장 반복 규칙·마무리 문제 3 | `doit-work/01-rules` | [규칙 템플릿](../chapter01/templates/AGENTS.template.md)을 AGENTS.md로 복사하거나 직접 작성 |
| 1장 마무리 문제 2 | `doit-work/01-template` | 템플릿만 만들 때는 시작 파일이 필요 없습니다. 채운 요약 요청을 실행할 때는 [document.md](../chapter01/examples/document.md)를 복사합니다. |
| 2장 첫 명령 → 같은 스레드 → 파일 태그 → diff | `doit-work/02-hello` | 첫 명령은 빈 폴더에서 시작합니다. hello.py를 만든 뒤 수정하고, 파일 태그 단계에서 [README.md](../chapter02/04_file_tag/start/README.md)만 추가합니다. |
| 2장 메모리 | `doit-work/02-memory` | 빈 폴더로 시작합니다. 가게 정보가 담긴 안내문·답안·AGENTS.md는 복사하지 않습니다. |
| 명령어 실행 전 검토 | `doit-work/02-command-check` | [plans.md](../chapter02/command_check/plans.md) |
| 2장 마무리 문제 1 | `doit-work/02-tag-review` | 하위 ch03 폴더를 만들고 [입력 자료 ex03_2.md](../ch03/ex03_2.md)만 복사합니다. |
| 2장 마무리 문제 2 | `doit-work/02-approval-a`, `02-approval-b`, `02-approval-c` | 비교할 방식마다 빈 폴더를 하나씩 사용합니다. |

같은 이름의 파일이 이미 있는 폴더는 새 실습용 이름으로 하나 더 만드세요. 시작 파일을 덮어써서 이전 결과를 지우지 않습니다.

2장 중간부터 시작할 때는 해당 실습의 `start` 파일을 새 `02-hello` 연습 폴더로 복사합니다. 이어서 진행할 때는 앞에서 수정한 hello.py를 유지합니다. `01-rules`의 AGENTS.md는 문서 원본 보존용이므로 hello.py를 직접 수정하는 폴더에 복사하지 않습니다.

관찰표를 작성하려면 실습 후 복사본에 기록합니다. 메모리 확인을 진행하는 동안에는 가게 정보와 답안을 그 작업 폴더로 가져오지 않습니다.

## 둘째마당

[둘째마당 작업 규칙](../part2/RULES.md)을 먼저 읽고 3~6장에 해당하는 폴더만 준비합니다.

3·5·6장의 새 실습은 별도 작업 폴더를 사용합니다. 예를 들어 `doit-work/03-meeting`, `05-monthly-report`, `06-candidates`처럼 구분하세요. 앞 단계의 결과를 이어 쓰는 실습은 장 안내에 따라 같은 폴더를 유지합니다. **4장의 파일 처리·메일 코드는 예외로 [4장 안내](../chapter04/README.md)에 따라 저장소 최상위를 열고 `work/ch04-xx`에 연습 복사본을 준비합니다.** 4장의 스킬 만들기는 `meeting_skill_practice`를 저장소 밖에 복사하고, 재사용은 같은 폴더를 유지하며, 마무리 문제는 별도 `moonlight_skill_practice`에서 진행합니다. 답안은 결과를 확인할 때 별도로 열어 보세요. 파일 이름 변경·분류 실습은 원본 보관 폴더 대신 연습용 복사본에서 진행합니다.
