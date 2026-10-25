# 서브에이전트 읽기 검수 카드

실습 48·49를 마친 뒤 `chapter14` 폴더를 연 상태에서 사용합니다. 경로는 `chapter14` 폴더를 기준으로 적었습니다.

## 역할 A — XML 구조 검사

- 읽을 파일: `recall_api/raw/recall_sample.xml`, `hazard_standard/raw/hazard_sample.xml`
- 결과 파일: `agent_a_xml_report.md`
- 확인: 행 수, 필드명, 빈 값, 원문 한 행
- 금지: 원본 수정, 안전 판단

## 역할 B — 공식 출처 검사

- 읽을 파일: `recall_api/source_metadata.json`, `hazard_standard/source_metadata.json`
- 결과 파일: `agent_b_source_report.md`
- 확인: 공식 도메인, 서비스 ID, 확인일, SHA-256
- 금지: 라이브 인증키 사용, 값 추정

## 역할 C — 안전 문구 검사

- 읽을 파일: `recall_api/output/recall_sample_author.csv`(실습 48 결과), `hazard_standard/hazard_standard_card.md`(실습 49 결과)
- 결과 파일: `agent_c_safety_report.md`
- 확인: 안전·진단·치료 단정, 샘플 표시, 확인 필요 문구
- 금지: 결과 파일 직접 수정

세 결과가 모두 돌아온 뒤 주 에이전트가 충돌표를 만들고, 독자가 최종 문장을 확정합니다.
