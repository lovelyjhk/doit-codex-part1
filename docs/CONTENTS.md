# 실습 자료 목록

첫째·둘째마당의 본문 실습과 마무리 문제에 필요한 자료입니다. 출판 준비 중인 초안이며, 수정 사항은 [변경 이력](../CHANGELOG.md)에서 확인할 수 있습니다.

| 책의 항목 | 문제·안내 | 시작 자료 | 결과·모범 답안 |
|---|---|---|---|
| 01-1 엑셀 합계 작업 예시 | [파일 작업](../chapter01/examples/file-task.md) | [CSV로 제공한 매출](../chapter01/examples/sales_2026.csv) | [합계 코드](../solutions/ch01/examples/sum_sales.py) |
| 01-2 좋은 프롬프트 6원칙 | [예시 프롬프트](../chapter01/examples/prompts.md) | [예시 자료](../chapter01/examples/README.md) | [결과 모음](../solutions/ch01/examples/README.md) |
| 01-3 반복 규칙 관리 | [사용 안내](../chapter01/templates/README.md) | [규칙 템플릿](../chapter01/templates/AGENTS.template.md) | [규칙 5줄 예시](../solutions/ch01/AGENTS.example.md) |
| 01-3 체크리스트·템플릿 | [템플릿](../chapter01/templates/prompts.md) | [체크리스트](../chapter01/templates/checklist.md) | [채운 사용 예](../solutions/ch01/ex01_2.md) |
| 1장 문제 1 부족한 프롬프트 고치기 | [문제](../chapter01/problems/ex01_1.md) | [보고서](../chapter01/examples/report.md), [문서](../chapter01/examples/document.md), [매출](../chapter01/examples/sales_2026.csv) | [답안](../solutions/ch01/ex01_1.md) |
| 1장 문제 2 내 업무용 템플릿 만들기 | [문제](../chapter01/problems/ex01_2.md) | [템플릿](../chapter01/templates/prompts.md) | [답안](../solutions/ch01/ex01_2.md) |
| 1장 문제 3 반복 규칙 파일 초안 작성 | [문제](../chapter01/problems/ex01_3.md) | 별도 빈 폴더 | [답안](../solutions/ch01/ex01_3.md) |
| 02-1 VS Code와 IDE 확장 설치 | [본문 실습 1](../chapter02/01_setup/README.md) | 빈 작업 폴더 | 같은 안내의 완료 기준 |
| 02-2 첫 번째 명령 | [본문 실습 2](../chapter02/02_first_command/README.md) | 빈 작업 폴더 | [hello.py](../solutions/ch02/02_first_command/hello.py) |
| 02-3 스레드와 메모리 | [본문 실습 3](../chapter02/03_thread_memory/README.md) | [hello.py](../chapter02/03_thread_memory/start/hello.py) | [모범 코드](../solutions/ch02/03_thread_memory/hello.py), [메모리 확인 기준](../solutions/ch02/03_thread_memory/memory-check.md) |
| 02-3 오늘의 추천 확장 예시 | [입력할 프롬프트](../chapter02/03_thread_memory/today-picks.md) | 시작 파일 없이 대화로 진행 | [3곡 조합 예시와 확인 기준](../solutions/ch02/03_thread_memory/today-picks.md) |
| 02-3 @ 파일 태그 | [본문 실습 4](../chapter02/04_file_tag/README.md) | [README.md](../chapter02/04_file_tag/start/README.md), [hello.py](../chapter02/04_file_tag/start/hello.py) | [답안](../solutions/ch02/04_file_tag/answer.md) |
| 02-3 diff | [본문 실습 5](../chapter02/05_diff/README.md) | [hello.py](../chapter02/05_diff/start/hello.py) | [모범 코드](../solutions/ch02/05_diff/hello.py), [diff](../solutions/ch02/05_diff/expected.diff) |
| 한 걸음 더 명령어 위험도 | [보충 예제](../chapter02/command_check/README.md) | [작업 계획](../chapter02/command_check/plans.md) | [답안](../solutions/ch02/command_check.md) |
| 2장 문제 1 @ 파일 태그 | [문제](../ch03/problems/ex03_2.md) | [ch03/ex03_2.md](../ch03/ex03_2.md) | [원고 경로의 답안](../solutions/ch03/ex03_2.md) |
| 2장 문제 2 승인 방식 | [문제](../ch03/problems/ex03_3.md) | 빈 연습 폴더, [관찰표](../ch03/approval-observation.md) | [원고 경로의 답안](../solutions/ch03/ex03_3.md) |

## hello.py 단계별 차이

| 단계 | 실행 동작 |
|---|---|
| 첫 명령 | `안녕하세요, Codex!` 출력 |
| 스레드 | 이름 입력 후 이름을 넣은 인사말과 오늘 날짜 출력 |
| 파일 태그 | 코드 실행을 바꾸지 않고 README를 참고해 작업 계획 정리 |
| diff | 이름 입력은 유지하고 인사말 한 줄을 `Hello, Do it! Codex!`로 변경 |

각 단계의 `start`는 시작 상태, `solutions`는 완료 상태입니다. 처음부터 모든 완료 파일을 한 폴더에 복사하지 않습니다.

## 둘째마당

| 장 | 실습과 자료 | 문제 | 답안 |
|---|---|---|---|
| 3장 문서·보고서 자동화 | [실습](../chapter03/README.md) | [문제](../chapter03/problems.md) | [답안](../solutions/part2/chapter03/README.md) |
| 4장 파일·반복 업무 자동화 | [실습](../chapter04/README.md) | [문제](../chapter04/problems.md) | [답안](../solutions/part2/chapter04/README.md) |
| 5장 데이터·엑셀 자동화 | [실습](../chapter05/README.md) | [문제](../chapter05/problems.md) | [답안](../solutions/part2/chapter05/README.md) |
| 6장 내 직군에서 시작하기 | [실습](../chapter06/README.md) | [문제](../chapter06/problems.md) | [답안](../solutions/part2/chapter06/README.md) |

[파일명으로 찾기](PART2_FILES.md)에서 같은 이름의 파일을 실습별 경로로 구분합니다.
