# [Do it! 실습] 회의록에서 결정 사항과 담당자 정리하기

여러 회의의 중복 내용을 합치고, 후속 회의에서 바뀐 마감일을 반영합니다.

1. 파일 탐색기에서 `doit-work/03-01_meeting` 폴더를 새로 만듭니다.
2. 아래 시작 파일을 모두 복사하고, VS Code의 **파일 → 폴더 열기**로 이 폴더를 엽니다.

- [meeting_notes_tue.md](start/meeting_notes_tue.md)
- [meeting_notes_thu.md](start/meeting_notes_thu.md)
- [recording_summary.txt](start/recording_summary.txt)

3. [입력할 프롬프트](prompts.md)를 순서대로 Codex에 입력합니다. 파일 이름 앞의 `@`는 입력 자료를 선택하는 파일 태그입니다. 선택이 어렵다면 같은 폴더에 있는 정확한 파일 이름을 적습니다.
4. `meeting_summary.md`를 열고 다음 항목을 원본과 비교합니다.

- [ ] 결정 사항이 5개 이내입니다.
- [ ] B대리 마감이 4월 15일입니다.
- [ ] C사원의 확인 방법을 추측하지 않았습니다.
- [ ] 리스크의 영향과 대응이 함께 있습니다.

5. 부족한 부분은 같은 대화에서 수정 요청을 보냅니다. 파일이 열리지 않으면 복사한 위치와 확장자를 확인합니다. [모범 답안](../../solutions/part2/chapter03/01_meeting/README.md)은 결과를 만든 뒤 비교하세요.

요청하는 역할은 요약의 독자를 정합니다. 입력 3개는 근거, 1페이지·표 구성은 결과 형식, 추측 금지와 원본 보존은 제약입니다. Markdown의 실제 인쇄 페이지 수는 글꼴과 인쇄 설정에 따라 달라집니다.

[3장 목록](../README.md)
