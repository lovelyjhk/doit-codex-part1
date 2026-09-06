# 모범 답안: 청크 처리

1. [chunk_sales.py](chunk_sales.py)를 CSV가 있는 연습 폴더로 복사합니다.
2. VS Code [터미널 → 새 터미널]에서 현재 폴더를 확인하고 실행합니다. Python 3가 설치되어 있어야 합니다. 추가 패키지는 필요 없습니다.

```powershell
python chunk_sales.py large_sales_sample.csv --chunk-size 200
```

3. 생성된 JSON을 [chunk_summary.json](chunk_summary.json)과 비교합니다. 데이터 2,400행, 청크 12개, 매출 12,120,000원, 수량 7,200개입니다. 매출은 지역별로 서울 2,940,000원·부산 3,000,000원·대전 3,060,000원·광주 3,120,000원입니다.
4. 다른 청크 크기로 다시 실행합니다. 원본과 기존 결과는 덮어쓰지 않습니다.

```powershell
python chunk_sales.py large_sales_sample.csv --chunk-size 137 --output chunk_137.json
```

이번에는 청크 18개입니다. 행 수와 합계는 같아야 합니다. `python`이 실행되지 않으면 설치한 Python 실행 경로 또는 `py` 명령을 사용하세요.

## 큰 파일로 확장하기

선택 실습입니다. [generate_large_sales.py](generate_large_sales.py)를 연습 폴더로 복사합니다. 기본 샘플과 다른 파일을 생성합니다. 먼저 디스크 여유 공간을 확인하세요.

```powershell
python generate_large_sales.py --rows 240000 --output large_sales_generated.csv
python chunk_sales.py large_sales_generated.csv --chunk-size 10000 --output generated_summary.json
```

240,000행의 매출 합계는 1,212,000,000원, 수량은 720,000개, 10,000행 단위 청크 수는 24개입니다. 100행마다 매출이 100~10,000원으로 반복되므로 한 묶음 합계 505,000원 × 2,400묶음으로 따로 검산합니다. 실제 수백 MB 파일을 저장소에 담지 않고 행 수를 정해 직접 확장할 수 있습니다.

[실습으로 돌아가기](../../../../chapter05/07_chunk_csv/README.md)
