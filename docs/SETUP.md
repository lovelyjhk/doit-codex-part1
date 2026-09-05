# 실습 환경 준비

## Windows에서 폴더와 파이썬 준비하기

1. 파일 탐색기에서 문서 폴더를 열고 `doit-work`라는 새 폴더를 만듭니다. [실습별 폴더 준비](WORK_FOLDERS.md)에 따라 이번 실습의 하위 폴더도 만듭니다. 첫 hello.py 실습은 `02-hello`입니다.
2. [VS Code 다운로드](https://code.visualstudio.com/Download)에서 PC에 맞는 Windows 설치 파일을 받아 설치합니다. **파일 → 폴더 열기**에서 방금 만든 **개별 실습 폴더**를 선택합니다. 첫 hello.py 실습에서는 `doit-work/02-hello`를 엽니다.
3. VS Code의 **터미널 → 새 터미널**을 선택합니다. 터미널은 프로그램 실행 명령을 입력하는 창입니다.
4. 다음 명령으로 파이썬이 설치되어 있는지 확인합니다.

```powershell
python --version
```

`Python 3.x.x`가 표시되면 준비되었습니다. 명령을 찾지 못하거나 Microsoft Store가 열리면 [Python 공식 Windows 다운로드](https://www.python.org/downloads/windows/)에서 Python 3을 설치한 뒤 VS Code를 다시 열어 확인합니다. `py --version`만 동작하는 PC에서는 아래 안내의 `python hello.py` 대신 `py hello.py`를 사용합니다.

5. 파이썬 파일은 `hello.py`라는 이름으로 저장합니다. `hello.py.txt`가 되지 않도록 파일 탐색기의 파일 확장명 표시를 켜 확인합니다.

이 저장소의 파이썬 예제에는 별도 패키지가 필요하지 않습니다. Python 3의 기본 기능만 사용합니다.

## 실행과 입력

터미널이 `hello.py`가 있는 폴더를 가리키는지 확인하고 실행합니다.

```powershell
python hello.py
```

`이름을 입력하세요:`가 나타나면 **터미널에** 이름을 입력하고 Enter를 누릅니다. 대화 입력창에 이름을 쓰면 실행 중인 프로그램으로 전달되지 않을 수 있습니다.

## 자주 만나는 오류

| 증상 | 확인 방법 |
|---|---|
| `can't open file` | VS Code 탐색기에 hello.py가 있는지, 터미널이 같은 폴더인지 확인합니다. |
| `EOFError` | 이름을 입력받는 프로그램을 일반 VS Code 터미널에서 다시 실행합니다. |
| 실행이 멈춘 것처럼 보임 | 이름을 기다리는 중인지 보고 터미널에 이름을 입력합니다. |
| `@` 목록에 파일이 안 보임 | 파일을 저장한 뒤 올바른 폴더를 열었는지 확인하고 경로를 직접 알려 줍니다. |
| Codex 아이콘이 안 보임 | `Ctrl+Shift+P`를 누르고 `Codex: Open Codex Sidebar`를 실행합니다. |

확장의 설치·로그인은 [본문 실습 1](../chapter02/01_setup/README.md)을 참고하세요.
