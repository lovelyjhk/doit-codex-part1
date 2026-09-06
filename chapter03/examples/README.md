# 문서 협업 규칙 예시

1. 새 `doit-work/03-document-rules` 폴더에 [AGENTS.template.md](AGENTS.template.md)를 `AGENTS.md`로 복사합니다.
2. [report_before.md](report_before.md)를 같은 폴더에 복사합니다.
3. 다음 문장을 입력합니다.

```text
AGENTS.md를 참고해 report_before.md의 띄어쓰기와 문장을 다듬어 줘.
수치와 뜻은 유지하고 report_review.md로 저장해. 변경 요약도 붙여 줘.
```

4. [모범 결과](../../solutions/part2/chapter03/examples/report_review.md)와 비교합니다.

Markdown에서는 색상과 Word 메모 표시를 동일하게 재현하기 어렵습니다. 이 예시는 `[수정: 사유]`, `[확인 필요]`, `~~기존 문장~~`으로 변경을 보여 줍니다. Word에서 실제 노란 강조·검토 메모를 연습할 때는 해당 서식을 지원하는 문서 파일과 편집 도구가 필요합니다.

## 외부 공유 전 보안 점검

[가상 보고서와 점검 프롬프트](security_review/README.md)를 사용해 본문·메모·변경 기록·문서 속성을 확인하고, 원문 값을 복사하지 않은 검토 기록을 만듭니다.
