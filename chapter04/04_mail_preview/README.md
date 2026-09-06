# [Do it! 실습] 작성한 메일의 발송 전 미리보기 준비하기

먼저 수신자·제목·본문을 파일로 미리 확인한 뒤, 필요할 때 **본인의 메일 서비스에서 직접 한 건만** 시험 발송합니다. 예제 코드는 로그인과 실제 발송을 자동화하지 않습니다.

1. [메일 초안](start/메일_초안.md)과 [발송 전 확인표](start/발송전_확인표.md)를 엽니다. 앞 실습에서 만든 초안을 사용해도 됩니다.
2. [프롬프트](prompts.md)로 미리보기와 드라이런 로그를 요청합니다. 또는 아래 코드를 실행합니다.

```powershell
python solutions/part2/chapter04/04_mail_preview/prepare_preview.py --draft chapter04/04_mail_preview/start/메일_초안.md --output work/ch04-04
```

3. `work/ch04-04/preview.md`를 열어 받는 사람 1개, 참조·숨은 참조 없음, 제목과 첨부 없음을 확인합니다. `dry_run.json`의 `sent`가 `false`인지 확인합니다. `.eml`은 메일 내용 저장 파일이며, 메일 앱에 따라 읽기 화면으로 열릴 수 있습니다.
4. 본인 메일함 시험이 필요하면 평소 쓰는 메일 서비스에 **직접** 로그인해 새 메일을 작성합니다. 받는 사람에 본인 주소 하나만 입력합니다. `preview.md`의 제목과 본문을 복사하고 첨부 없이 준비합니다. `me@example.com`으로 보내지 마세요.
5. 확인표의 미확인 항목을 직접 검토한 뒤, 본인이 [보내기]를 누릅니다. 받은 편지함이나 스팸함에서 도착 여부·제목·한글 표시를 확인해 개인 작업용 기록에 적습니다.

이 저장소에는 본인의 주소, 비밀번호, API 키, 도착 화면을 저장하지 않습니다. 시험에 성공해도 거래처 전체 발송으로 확대하는 단계는 이 실습에 포함하지 않습니다.

## 자동화 안전장치 살펴보기

본문에서 소개한 네 가지 장치는 [안전장치 예제](../../solutions/part2/chapter04/04_mail_preview/guarded_demo.py)로 외부 발송 없이 확인할 수 있습니다. 30분 이내 재실행·하루 3회 초과 실행을 막고, 기본은 미리보기이며, 이상 발생은 로컬 로그에 남깁니다. 협업 도구 알림은 실제 연결과 발송 승인이 필요한 별도 작업입니다.

```powershell
python solutions/part2/chapter04/04_mail_preview/guarded_demo.py --state work/ch04-04/guard_state.json
python solutions/part2/chapter04/04_mail_preview/guarded_demo.py --state work/ch04-04/guard_state.json --confirm RUN
```

두 번째 명령을 바로 다시 실행하면 차단됩니다. 이 명령도 실제 메일을 보내지 않습니다.

[완료 예제](../../solutions/part2/chapter04/04_mail_preview/README.md)
