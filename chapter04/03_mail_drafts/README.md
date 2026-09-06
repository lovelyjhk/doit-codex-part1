# [Do it! 실습] 거래처에 보낼 안내 메일 초안 만들기

20개 가상 거래처의 회사명과 호칭을 반영한 초안을 만듭니다. 원고에서 생성해 보도록 안내한 CSV를 [시작 파일](start/거래처_샘플.csv)로 미리 제공합니다. [가상 업무 메모](start/분기_안내_메모.md)를 함께 읽으면 실적과 일정을 지어내지 않고 작성할 수 있습니다.

1. CSV를 VS Code에서 열어 첫 줄의 열 이름과 20개 데이터 행을 확인합니다. Excel로 열 때도 한국어를 읽을 수 있도록 UTF-8 BOM을 사용했습니다.
2. [목록 확인과 초안 생성 프롬프트](prompts.md)를 순서대로 실행합니다.
3. 생성된 `work/ch04-03/drafts`에서 1·5·10·15·20번 초안을 열어 회사명·이름·호칭을 CSV와 비교합니다.
4. 각 초안의 첨부 파일·회신 마감일·최종 승인자가 `[확인 필요]`인지 확인합니다. ‘님님’처럼 호칭이 중복되면 해당 조건을 고쳐 다시 요청합니다.

## 답안 코드로 확인하기

```powershell
python solutions/part2/chapter04/03_mail_drafts/make_drafts.py --recipients chapter04/03_mail_drafts/start/거래처_샘플.csv --output work/ch04-03/drafts
```

기존 출력 폴더가 있으면 덮어쓰지 않고 멈춥니다. 다시 실행하려면 `--output work/ch04-03/drafts-v2`처럼 새 위치를 지정합니다. 스크립트의 본문은 제공된 가상 업무 메모 내용으로 고정되어 있으며 실제 발송 기능은 없습니다.

정상 결과: Markdown 초안 20개. 제목은 `[검토용 초안] 2026년 3분기 협업 결과와 다음 일정 안내`입니다.

[모범 답안과 20개 초안](../../solutions/part2/chapter04/03_mail_drafts/README.md)
