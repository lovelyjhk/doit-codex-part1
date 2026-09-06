# [Do it! 실습] 파일 이름 한 번에 바꾸기

Twemoji PNG 다섯 개를 `photo_YYYYMMDD_001.png` 형식으로 바꿉니다. 이 파일에는 EXIF 촬영일이 없으므로 **실행하는 날의 한국 날짜**를 사용합니다.

1. 빈 연습 폴더 `work/ch04-01`을 만들고 [PNG 시작 자료](start/png/)를 그 안에 복사합니다. `work/ch04-01/png`에 PNG 5개와 `image_sources.txt`가 보이면 준비되었습니다. 직접 내려받으려면 [다운로드 프롬프트](prompts.md)를 사용합니다.
2. [이름 변경 프롬프트](prompts.md)를 입력합니다. 코덱스가 실제 작업 폴더의 전체 경로와 다섯 파일의 변경표를 보여 줄 때까지 기다립니다. 아직 적용하지 않습니다.
3. 원래 이름 오름차순, 한국 실행일, `.png` 확장자, 충돌 여부를 확인합니다. PNG 다섯 개만 대상이고 `image_sources.txt`는 그대로인지 확인한 뒤 적용을 요청합니다.
4. 변경 후 다섯 PNG가 열리는지, 변경 전후 SHA-256이 일치하는지 확인합니다. SHA-256은 파일 내용에서 계산한 지문입니다. 파일 이름만 바꾸면 같은 값이 나와야 합니다.

## 답안 코드로 확인하기

저장소 최상위에서 다음 명령으로 계획만 만듭니다. 날짜를 생략하면 한국 실행일을 사용합니다.

```powershell
python solutions/part2/chapter04/file_ops.py plan png --root work/ch04-01/png --plan work/ch04-01/rename_plan.json
```

표를 검토해 승인할 때만 다음 명령을 실행합니다.

```powershell
python solutions/part2/chapter04/file_ops.py apply --root work/ch04-01/png --plan work/ch04-01/rename_plan.json --receipt work/ch04-01/rename_receipt.json --confirm APPLY
```

복구도 표를 먼저 보고 적용합니다.

```powershell
python solutions/part2/chapter04/file_ops.py undo --root work/ch04-01/png --receipt work/ch04-01/rename_receipt.json
python solutions/part2/chapter04/file_ops.py undo --root work/ch04-01/png --receipt work/ch04-01/rename_receipt.json --confirm UNDO
```

정상 결과는 변경 5개, 다른 파일 변경 0개입니다. 파일이 빠졌거나 내용이 바뀌었으면 원인을 확인한 뒤 새 계획을 만듭니다. 기존 결과에 덮어 실행하지 마세요.

[모범 변경표](../../solutions/part2/chapter04/01_rename_photos/README.md)

`start/photos`의 가상 JPG는 이전 EXIF 예시를 보존한 보충 자료입니다. 현재 본문 실습에서는 `start/png`만 사용합니다.
