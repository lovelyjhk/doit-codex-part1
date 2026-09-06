# [Do it! 실습] 다운로드 폴더를 종류별로 나누기

문서와 이미지가 뒤섞인 연습용 폴더를 정리합니다. **실제 다운로드 폴더가 아닌 제공된 복사본**을 사용합니다.

1. [start](start/)를 `work/ch04-02`로 복사합니다.
2. GitHub에서 내려받으면 파일 수정일이 달라지므로 아래 명령으로 복사본의 연습 날짜를 먼저 맞춥니다. 파일 내용은 바뀌지 않습니다. 기준일은 `2026-09-05`, 오래된 기준은 `2025-09-05`까지입니다.

```powershell
python chapter04/02_sort_downloads/set_sample_dates.py --root work/ch04-02/downloads --confirm APPLY
```

3. [미리 보기 프롬프트](prompts.md)를 입력해 이동표와 보류 목록을 확인합니다. 임시 파일은 오래됐더라도 보류가 우선입니다.
4. 변경 계획을 확인한 뒤 적용 요청을 입력합니다. `pdf`, `docx`, `xlsx`, `이미지`, `기타`, `_archive` 폴더와 남아 있는 임시 파일을 확인합니다.

## 답안 코드로 확인하기

```powershell
python solutions/part2/chapter04/file_ops.py plan sort --root work/ch04-02/downloads --today 2026-09-05 --plan work/ch04-02/sort_plan.json
python solutions/part2/chapter04/file_ops.py apply --root work/ch04-02/downloads --plan work/ch04-02/sort_plan.json --receipt work/ch04-02/sort_receipt.json --confirm APPLY
```

복구할 때는 먼저 표를 보고 승인합니다. 복구 후 생긴 빈 분류 폴더는 남습니다.

```powershell
python solutions/part2/chapter04/file_ops.py undo --root work/ch04-02/downloads --receipt work/ch04-02/sort_receipt.json
python solutions/part2/chapter04/file_ops.py undo --root work/ch04-02/downloads --receipt work/ch04-02/sort_receipt.json --confirm UNDO
```

1년은 365일 고정이 아니라 전년도 같은 날짜까지로 계산합니다. 2월 29일 기준이면 전년 2월 28일을 경계로 삼습니다. 실제 자료를 정리할 때에는 기준일을 바꾸고 미리보기를 새로 만드세요.

[모범 이동표](../../solutions/part2/chapter04/02_sort_downloads/README.md)
