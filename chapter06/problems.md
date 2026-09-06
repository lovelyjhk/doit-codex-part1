# 6장 마무리 문제

## 1. 내 업무 자료 한 가지 정리하기

- **문제 제목**: 내 업무 자료 한 가지 정리하기 ★
- **문제 내용**: 업무명, 마감일, 우선순위, 확인할 항목을 표로 정리해 `weekly_tasks_summary.md`로 저장하세요. 업무 다섯 개를 모두 포함하고 원문에 없는 마감일과 우선순위는 `[확인 필요]`로 남깁니다.
- **필요 파일**: [chapter06/weekly_tasks_sample.md](weekly_tasks_sample.md)
- **모범 답안 파일**: [solutions/part2/chapter06/weekly_tasks_summary.md](../solutions/part2/chapter06/weekly_tasks_summary.md)

1. [weekly_tasks_sample.md](weekly_tasks_sample.md)를 새 작업 폴더에 복사합니다. VS Code에서 그 폴더를 여세요.
2. 아래 프롬프트에서 `@weekly_tasks_sample.md` 파일을 선택한 뒤 요청합니다.

```text
너는 반복 업무 정리 도우미야.
@weekly_tasks_sample.md만 읽고 weekly_tasks_summary.md를 새로 만들어 줘.
업무명, 마감일, 우선순위, 확인할 항목을 표로 정리해 줘.
자료에 없는 내용은 추정하지 말고 [확인 필요]로 남겨 줘.
원본은 수정하지 말고 실제 업무를 실행하지 마.
```

3. 업무가 다섯 개 모두 들어 있는지 확인합니다. 원문에는 마감일과 우선순위가 없으므로 임의로 정하지 않아야 합니다.

## 2. 반복해서 쓸 프롬프트로 다듬기

- **문제 제목**: 반복해서 쓸 프롬프트로 다듬기 ★
- **문제 내용**: 앞 문제의 프롬프트에 `[입력 파일]`, `[결과 파일]`, `[확인 항목]`을 넣어 `reusable_prompt.md`로 저장하세요. 원본 보존과 미확정 값 표시를 유지하고 실제 값으로 바꾸어 `weekly_tasks_summary_retry.md`를 만든 뒤 업무 누락과 임의 생성 여부를 대조하세요.
- **필요 파일**: [chapter06/weekly_tasks_sample.md](weekly_tasks_sample.md), 앞 문제의 프롬프트
- **모범 답안 파일**: [solutions/part2/chapter06/reusable_prompt.md](../solutions/part2/chapter06/reusable_prompt.md), [재실행 결과](../solutions/part2/chapter06/weekly_tasks_summary_retry.md)

1. 앞 문제의 프롬프트를 `[입력 파일]`, `[결과 파일]`, `[확인 항목]` 자리표시자로 바꾸어 `reusable_prompt.md`에 저장해 보세요.
2. 아래 조건이 있는지 확인합니다: 지정 입력만 사용, 원본 보존, 미확정 값 표시, 결과 파일과 확인 기준 지정.
3. 자리표시자를 앞 문제의 실제 파일명과 항목으로 바꿔 새 스레드에서 사용할 수 있는지 읽어 봅니다. 이미 만든 결과를 덮어쓰지 않도록 결과 이름을 `weekly_tasks_summary_retry.md`로 바꾸세요.

[모범 답안](../solutions/part2/chapter06/problems.md) · [6장으로 돌아가기](README.md)
