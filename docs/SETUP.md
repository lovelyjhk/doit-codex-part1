# 실습 환경 준비

공통 준비를 마친 뒤 현재 공부하는 마당의 규칙을 따릅니다.

- [첫째마당 작업 규칙](../part1/RULES.md): 1~2장, 독립 실습과 이어서 하는 단계를 구분
- [둘째마당 작업 규칙](../part2/RULES.md): 3~6장, 시작 자료 위치와 4장 작업 위치 예외 확인

## 공통 Windows 준비

1. [VS Code 다운로드](https://code.visualstudio.com/Download)에서 PC에 맞는 Windows 설치 파일을 받아 설치합니다.
2. 파일 탐색기에서 문서 폴더 아래에 `doit-work`를 만듭니다. 현재 마당의 작업 규칙과 [실습별 폴더 준비](WORK_FOLDERS.md)에서 이번에 열 폴더를 확인합니다.
3. VS Code의 **파일 → 폴더 열기**에서 지정한 폴더를 엽니다. 실습마다 실행 위치가 다를 수 있으므로 임의로 저장소 전체나 이전 연습 폴더를 열지 않습니다.
4. Codex 확장의 설치·로그인이 아직 끝나지 않았다면 [첫째마당 설치 실습](../chapter02/01_setup/README.md)을 따라 준비합니다.

## 첫째마당 hello.py 실행 준비

첫째마당의 파이썬 예제는 Python 3의 기본 기능만 사용합니다.

1. `doit-work/02-hello`를 만들고 VS Code에서 엽니다.
2. **터미널 → 새 터미널**을 선택합니다. 터미널은 프로그램 실행 명령을 입력하는 창입니다.
3. 다음 명령으로 파이썬이 설치되어 있는지 확인합니다.

```powershell
python --version
```

`Python 3.x.x`가 표시되면 준비되었습니다. 명령을 찾지 못하거나 Microsoft Store가 열리면 [Python 공식 Windows 다운로드](https://www.python.org/downloads/windows/)에서 Python 3을 설치한 뒤 VS Code를 다시 엽니다. `py --version`만 동작하는 PC에서는 아래 안내의 `python hello.py` 대신 `py hello.py`를 사용합니다.

4. 파이썬 파일은 `hello.py`라는 이름으로 저장합니다. `hello.py.txt`가 되지 않도록 파일 탐색기의 파일 확장명 표시를 켜 확인합니다.
5. 터미널이 `hello.py`가 있는 폴더를 가리키는지 확인하고 실행합니다.

```powershell
python hello.py
```

`이름을 입력하세요:`가 나타나면 **터미널에** 이름을 입력하고 Enter를 누릅니다. 대화 입력창에 이름을 쓰면 실행 중인 프로그램으로 전달되지 않을 수 있습니다.

### hello.py에서 자주 만나는 오류

| 증상 | 확인 방법 |
|---|---|
| `can't open file` | VS Code 탐색기에 hello.py가 있는지, 터미널이 같은 폴더인지 확인합니다. |
| `EOFError` | 이름을 입력받는 프로그램을 일반 VS Code 터미널에서 다시 실행합니다. |
| 실행이 멈춘 것처럼 보임 | 이름 입력을 기다리는 중인지 보고 터미널에 이름을 입력합니다. |

## 둘째마당 추가 준비

둘째마당의 문서 요약과 후보표 작성은 파이썬 코드 실행 없이 진행할 수 있습니다. 파일 처리·엑셀·그래프 예제에는 Python이나 Pillow, openpyxl, matplotlib 등의 패키지가 필요할 수 있습니다. 코드를 실행하는 실습에서 해당 README와 `requirements.txt`에 적힌 항목만 설치하세요.

4장의 파일 처리·메일 코드와 스킬 실습은 작업 위치가 다릅니다. [둘째마당 작업 규칙의 4장 예외](../part2/RULES.md#4장-실행-위치-예외)를 먼저 확인합니다.

## Codex 확장에서 자주 만나는 오류

| 증상 | 확인 방법 |
|---|---|
| `@` 목록에 파일이 안 보임 | 파일을 저장한 뒤 올바른 폴더를 열었는지 확인하고 경로를 직접 알려 줍니다. |
| Codex 아이콘이 안 보임 | `Ctrl+Shift+P`를 누르고 `Codex: Open Codex Sidebar`를 실행합니다. |

[저장소 처음으로](../README.md)
