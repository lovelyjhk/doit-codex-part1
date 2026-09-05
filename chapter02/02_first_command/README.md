# [Do it! 실습] 코덱스에게 첫 번째 명령 내리기

시작 상태는 빈 작업 폴더입니다. Codex가 `hello.py`를 직접 만드는 과정을 확인합니다.

1. VS Code에서 실습용 빈 폴더를 열고 다음 문장을 입력합니다.

```text
hello.py 파일을 만들고 "안녕하세요, Codex!"를 출력하는 코드를 작성해 줘.
```

2. 탐색기에 `hello.py`가 생겼는지 확인하고 열어 코드를 읽습니다.
3. 같은 스레드에 다음 문장을 입력합니다.

```text
hello.py를 실행해서 결과를 보여 줘.
```

4. 출력이 아래 문장과 같은지 확인합니다.

```text
안녕하세요, Codex!
```

명령 실행이 안 되면 [환경 준비](../../docs/SETUP.md)를 참고해 터미널에서 `python hello.py`를 실행합니다. `print`는 문장을 화면에 출력하는 파이썬 기능입니다.

[모범 코드](../../solutions/ch02/02_first_command/hello.py) · [다음 실습](../03_thread_memory/README.md)
