# 읽기 전용 문서 점검 MCP

반복 공백, 연속 문장부호, 빈 대괄호와 일부 용어 표기 후보를 찾는 교육용 STDIO MCP입니다. 맞춤법 전체나 계약의 의미·효력을 판단하지 않습니다.

## 연결 전에 확인하세요

도구 설명과 조회 결과가 길거나 도구를 반복 호출하면 토큰 사용량이 늘 수 있습니다. 무료 플랜으로 처음 실습할 때는 MCP 연결을 선택 단계로 남겨 두고, 원고 7장의 일반 프롬프트로 파일을 점검하는 방법부터 익히세요. 필요한 경우 자신의 사용량 한도와 연결할 도구의 접근 권한을 확인한 뒤 진행합니다.

이 서버는 파일을 읽어 검사 결과를 반환하고 파일을 수정하지 않습니다. 읽기 전용이어도 읽은 내용과 결과가 코덱스에 전달될 수 있으므로 가상 예제나 민감정보를 가린 실습 자료만 사용합니다. 인증 키와 비밀번호는 프롬프트·실습 파일·화면 캡처에 넣지 않습니다.

## Windows와 VS Code에서 준비하기

1. 제공된 chapter07/contract 폴더를 복사하고 VS Code의 [파일 → 폴더 열기]로 복사 폴더를 엽니다.
2. [터미널 → 새 터미널]에서 다음 명령을 각각 입력합니다.

```powershell
node --version
npm.cmd --version
```

Node.js 20 이상이 필요합니다. 명령을 찾을 수 없다면 [Node.js 공식 다운로드](https://nodejs.org/en/download)에서 LTS 버전의 Windows 설치 파일을 받아 설치하고 VS Code를 다시 엽니다.

3. 터미널의 현재 위치가 contract 폴더인지 확인한 뒤 다음 명령을 한 줄씩 실행합니다.

```powershell
cd document-check-mcp
npm.cmd ci
npm.cmd run check
```

4. 탐색기에서 server.mjs를 마우스 오른쪽 버튼으로 클릭하고 [경로 복사]를 선택합니다.
5. 코덱스 설정의 [MCP servers → Add server]에서 이름 document_check, 방식 STDIO, 명령 node를 입력합니다. 인수에는 복사한 server.mjs의 전체 경로를 넣고 저장한 뒤 코덱스 확장을 다시 시작합니다. 코덱스가 서버 프로세스를 실행하므로 별도 터미널에서 npm start를 함께 실행할 필요는 없습니다.

[IDE MCP 연결 공식 안내](https://learn.chatgpt.com/docs/extend/mcp?surface=ide)를 참고하세요.

## 검사할 경로와 응답

check_document의 relative_path는 contract 폴더를 기준으로 적습니다.

- sample_contract.txt: 표기 오류를 넣은 가상 예제입니다.
- missing_document.txt: 없는 파일이므로 오류로 거부되어야 합니다.
- ../outside.txt: 허용 폴더 밖 경로이므로 거부되어야 합니다.
- work/contract_draft.md: 원고의 앞 단계에서 실제로 만든 초안을 검사할 때 사용합니다.

정상 응답의 검사 대상과 후보 목록을 읽고, 도구를 호출하지 못했으면 오류를 기록합니다. MCP 미연결 상태의 코덱스 읽기 점검을 MCP 실행 성공으로 표시하지 않습니다.

운영체제가 허용하는 환경에서는 실습 폴더 안의 링크·정션이 바깥 파일을 가리킬 때도 거부되는지 별도로 시험할 수 있습니다.

readOnlyHint는 도구의 성격을 설명하는 정보이며 권한 제한을 보장하는 보안 장치가 아닙니다. 이 예제는 realpath로 허용 폴더를 확인하고 검사 파일을 수정하지 않습니다. 다른 MCP를 연결할 때는 제공자·배포 경로·읽기/쓰기 권한·외부 전송 범위를 따로 확인하세요.

[사용량 안내](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) · [MCP의 데이터 전송과 보안](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)
