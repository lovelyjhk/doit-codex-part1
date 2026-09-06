# 지점 자료에서 7월 실적을 뽑고 빠진 지역 확인하기 참고 결과

학습용 가상 자료를 실제 계산하고 저장한 참고 결과입니다. Codex 대화 화면 캡처는 아닙니다.

- [july-branch-check.xlsx](july-branch-check.xlsx)
- [chunk-log.txt](chunk-log.txt)

200행씩 5개 묶음, 전체 1,000행, 선택 125행, 다른 기간 875행입니다. 광주 4,040,000원·996개이며 다른 세 지역의 금액과 수량은 빈칸이어야 합니다. 첫 묶음 선택 매출은 786,250원, 선택 날짜는 7월 3~27일입니다.

[입력과 프롬프트](../../../../chapter05/10_branch_report/README.md)

파이썬으로 집계 과정을 직접 확인하려면 [extract_july.py](extract_july.py)를 사용합니다. Python 표준 라이브러리만 사용하며 별도 패키지는 필요 없습니다. 저장소 최상위 폴더에서 다음 명령을 실행합니다.

```powershell
python solutions/part2/chapter05/10_branch_report/extract_july.py chapter05/inputs/large_sales_sample.csv --chunk-size 200 --output results/july-200
python solutions/part2/chapter05/10_branch_report/extract_july.py chapter05/inputs/large_sales_sample.csv --chunk-size 100 --output results/july-100
```

각 새 폴더에 선택한 원본 행 `selected.csv`, 집계 `summary.json`, 처리 기록 `chunk-log.txt`가 만들어집니다. 이 스크립트는 CSV 집계 단계의 참고 소스입니다. XLSX까지 다시 만들려면 위의 입력과 프롬프트 안내대로 코덱스에 요청하고, 필요한 실행 준비를 확인한 뒤 승인합니다. XLSX는 내려받을 수 있는 참고 결과도 제공합니다.

두 명령의 최종 행 수·합계는 같아야 합니다. 기존 결과가 있는 폴더에는 덮어쓰지 않으므로 새 출력 폴더를 지정하세요. 날짜·숫자·빈 값 오류가 생기면 행 위치를 알리고 중단하며, 해당 폴더의 중간 결과를 완성 보고서로 사용하지 않습니다.
