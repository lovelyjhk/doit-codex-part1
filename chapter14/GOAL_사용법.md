# /goal 사용 안내

`/goal`은 한 번의 응답으로 끝나지 않는 작업을 검증 가능한 종료 조건까지 이어 갈 때 사용합니다. 단순 질문이나 서로 관련 없는 할 일 목록에는 사용하지 않습니다.

## 시작하기

```text
/goal chapter14의 공식 샘플 XML 두 파일은 수정하지 않고 CSV와 안전 여부를 단정하지 않는 설명 카드를 완성하세요. source_metadata.json의 URL·서비스 ID·SHA-256을 확인하고, 결과 행 수와 원문 대조 기록이 모두 통과하면 멈추세요.
```

좋은 목표에는 다음 네 가지가 들어갑니다.

- 바꿀 범위와 바꾸지 말아야 할 원본
- 먼저 읽을 파일
- 결과물과 검증 방법
- 작업을 멈출 조건

긴 지시는 별도 파일에 적고 목표에서 그 파일을 가리키세요.

## 상태 제어

```text
/goal
/goal pause
/goal resume
/goal clear
```

- `/goal`: 현재 목표와 진행 상태를 확인합니다.
- `/goal pause`: 진행을 잠시 멈춥니다.
- `/goal resume`: 같은 목표를 다시 이어 갑니다.
- `/goal clear`: 끝난 목표를 지웁니다.

## 명령이 보이지 않을 때

Goals를 지원하는 코덱스 환경에서 사용합니다. 명령이 보이지 않으면 CLI에서 다음 명령을 실행합니다.

```text
codex features enable goals
```

또는 `config.toml`에 다음 설정을 추가한 뒤 코덱스를 다시 시작합니다.

```toml
[features]
goals = true
```

기능을 지원하지 않는 환경에서는 `CONTEXT.md`에 목표, 입력 파일, 완료 조건, 진행 상태를 기록하고 일반 프롬프트로 작업을 이어 갑니다.

공식 문서(2026-10-25 확인): https://learn.chatgpt.com/use-cases/follow-goals
