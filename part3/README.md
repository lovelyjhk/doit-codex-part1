# 셋째마당 · 생활 속에서 코덱스 활용하기

셋째마당은 7~10장입니다. 계약서·보험증권·이력서·직구 가격·여행 정보·출판 자료를 코덱스로 정리하고, 원문과 공식 자료로 다시 확인하는 방법을 연습합니다. 모든 시작 자료는 교육용 가상 자료입니다.

## 이 순서로 시작하세요

1. 저장소의 **Code → Download ZIP**으로 자료를 내려받고 압축을 풉니다.
2. 아래 표에서 실습의 **VS Code에서 열 폴더**를 작업할 위치에 복사합니다. 내려받은 원래 폴더는 그대로 보관합니다.
3. VS Code의 [파일 → 폴더 열기]로 복사한 폴더를 엽니다. 왼쪽 탐색기에 시작 파일이 보이면 준비가 된 것입니다.
4. [셋째마당 프롬프트](PROMPTS.md)에서 해당 실습의 프롬프트를 단계 순서대로 입력합니다.
5. 마무리 문제를 푼 뒤 모범 답안과 비교합니다.

## 작업 규칙

- 책의 파일 경로는 VS Code에서 연 폴더를 기준으로 씁니다. 슬래시(/) 앞은 폴더, 뒤는 파일 이름입니다.
- 프롬프트의 `@파일명`은 입력란에 `@`를 입력한 뒤 목록에서 그 파일을 고르라는 뜻입니다. 아직 만들지 않은 결과 파일은 `@` 없이 이름만 적습니다.
- 실습의 첫 프롬프트에 있는 "너는 ○○ 도우미야."는 그 실습에서 코덱스가 맡을 역할입니다. 같은 대화에서 이어지는 단계에는 다시 쓰지 않습니다.
- 원본 시작 파일은 수정하지 않고, 결과는 새 파일로 만듭니다. 책에서 '사본'은 복사한 작업 폴더 안의 파일을 뜻합니다.
- 근거가 없는 값은 추정하지 않고 확인 필요로 남깁니다. 계약·보험·구매·여행·출판의 최종 판단은 원문과 공식 안내를 확인해 직접 내립니다.
- 실제 이름·주소·연락처·계좌·계정 정보와 인증 키는 프롬프트와 실습 파일에 넣지 않습니다.
- 로그인·결제·업로드·발행·메일 발송처럼 외부 상태를 바꾸는 일은 코덱스에 맡기지 않고 직접 확인하고 실행합니다.

### 7장 MCP 실습 준비

계약서 실습의 MCP 연결은 선택 단계입니다. Node.js 20 이상과 npm이 필요하며, 설치·연결·시험 순서는 [document-check-mcp/README.md](../chapter07/contract/document-check-mcp/README.md)에 있습니다. 연결이 어렵다면 책의 6단계에 있는 읽기 전용 점검 프롬프트로 이어 가도 됩니다.

## 본문 실습

| 장 | 실습 | VS Code에서 열 폴더 | 시작 파일 | 프롬프트 |
|---|---|---|---|---|
| 7장 | 계약서 초안을 만들고 문서 확인 MCP로 검수하기 | [`chapter07/contract`](../chapter07/contract/) | [sample_contract_notes.md](../chapter07/contract/sample_contract_notes.md), [sample_contract.txt](../chapter07/contract/sample_contract.txt), [README.md](../chapter07/contract/document-check-mcp/README.md) | [보기](PROMPTS.md#do-it-실습-계약서-초안을-만들고-문서-확인-mcp로-검수하기) |
| 7장 | 보험증권의 핵심 항목과 확인 질문 찾기 | [`chapter07/insurance`](../chapter07/insurance/) | [sample_policy.txt](../chapter07/insurance/sample_policy.txt), [insurance_checklist.md](../chapter07/insurance/insurance_checklist.md) | [보기](PROMPTS.md#do-it-실습-보험증권의-핵심-항목과-확인-질문-찾기) |
| 8장 | 실습 36 내 경력 메모로 이력서 초안 만들기 | [`chapter08`](../chapter08/) | [author_career_notes_template.md](../chapter08/resume/author_career_notes_template.md), [job_posting_sample.md](../chapter08/resume/job_posting_sample.md) | [보기](PROMPTS.md#do-it-실습-36-내-경력-메모로-이력서-초안-만들기) |
| 8장 | 실습 37 직구 상품의 실제 예상 비용 조회하기 | [`chapter08`](../chapter08/) | [price_offers_sample.csv](../chapter08/price/price_offers_sample.csv), [price_check_rules.md](../chapter08/price/price_check_rules.md), [price_source_log.csv](../chapter08/price/price_source_log.csv) | [보기](PROMPTS.md#do-it-실습-37-직구-상품의-실제-예상-비용-조회하기) |
| 9장 | 실습 38 공식 자료로 따라 하기 쉬운 여행 일정표 만들기 | [`chapter09`](../chapter09/) | [travel_request_template.md](../chapter09/travel/travel_request_template.md), [travel_source_log.csv](../chapter09/travel/travel_source_log.csv), [official_source_seed.csv](../chapter09/travel/official_source_seed.csv) | [보기](PROMPTS.md#do-it-실습-38-공식-자료로-따라-하기-쉬운-여행-일정표-만들기) |
| 9장 | 실습 39 MCP 서버 정보를 비교하는 교육용 안내 카탈로그 만들기 | [`chapter09`](../chapter09/) | [mcp_catalog_sample.json](../chapter09/mcp-market/mcp_catalog_sample.json), [starter.html](../chapter09/mcp-market/starter.html), [verification_log.csv](../chapter09/mcp-market/verification_log.csv) | [보기](PROMPTS.md#do-it-실습-39-mcp-서버-정보를-비교하는-교육용-안내-카탈로그-만들기) |
| 10장 | 실습 40 아마존 KDP에 Kindle 전자책 발행하기 | [`chapter10`](../chapter10/) | [kdp_metadata_template.md](../chapter10/amazon-kdp/kdp_metadata_template.md), [kdp_preflight.md](../chapter10/amazon-kdp/kdp_preflight.md), [ai_use_log.md](../chapter10/amazon-kdp/ai_use_log.md), [rights_and_assets_log.csv](../chapter10/amazon-kdp/rights_and_assets_log.csv) | [보기](PROMPTS.md#do-it-실습-40-아마존-kdp에-kindle-전자책-발행하기) |
| 10장 | 실습 41 교보문고 바로출판 POD로 종이책 출판하기 | [`chapter10`](../chapter10/) | [kyobo_metadata_template.md](../chapter10/kyobo-pod/kyobo_metadata_template.md), [kyobo_pod_preflight.md](../chapter10/kyobo-pod/kyobo_pod_preflight.md), [rights_and_assets_log.csv](../chapter10/kyobo-pod/rights_and_assets_log.csv) | [보기](PROMPTS.md#do-it-실습-41-교보문고-바로출판-pod로-종이책-출판하기) |

## 마무리 문제

| 장 | 마무리 문제 | 실습 파일 | 모범 답안 |
|---|---|---|---|
| 7장 | 1. 계약서 표기 오류 점검표 만들기 ★ | [sample_contract.txt](../chapter07/contract/sample_contract.txt) | [practice_contract_review.md](../chapter07/answers/practice_contract_review.md) |
| 7장 | 2. 보험증권 핵심 항목과 확인 질문 정리하기 ★★ | [sample_policy.txt](../chapter07/insurance/sample_policy.txt) | [practice_insurance_summary.md](../chapter07/answers/practice_insurance_summary.md), [practice_insurance_questions.md](../chapter07/answers/practice_insurance_questions.md) |
| 8장 | 1. 이력서 문장 사실 확인표 만들기 ★ | [author_career_notes_template.md](../chapter08/resume/author_career_notes_template.md) | [chapter08_practice_answers.md](../chapter08/answers/chapter08_practice_answers.md) |
| 8장 | 2. 총비용이 보이는 가격 비교표 만들기 ★★ | [price_offers_sample.csv](../chapter08/price/price_offers_sample.csv) | [chapter08_practice_answers.md](../chapter08/answers/chapter08_practice_answers.md) |
| 9장 | 1. 공식 출처가 있는 여행 일정표 만들기 ★ | [travel_request_template.md](../chapter09/travel/travel_request_template.md) | [chapter09_practice_answers.md](../chapter09/answers/chapter09_practice_answers.md) |
| 9장 | 2. MCP 안내 카탈로그 검증표 만들기 ★★ | [mcp_catalog_sample.json](../chapter09/mcp-market/mcp_catalog_sample.json) | [chapter09_practice_answers.md](../chapter09/answers/chapter09_practice_answers.md) |
| 10장 | 1. 전자책 출판 전 점검표 만들기 ★ | [kdp_preflight.md](../chapter10/amazon-kdp/kdp_preflight.md) | [chapter10_practice_answers.md](../chapter10/answers/chapter10_practice_answers.md) |
| 10장 | 2. POD 제출 전 점검표 만들기 ★★ | [kyobo_pod_preflight.md](../chapter10/kyobo-pod/kyobo_pod_preflight.md) | [chapter10_practice_answers.md](../chapter10/answers/chapter10_practice_answers.md) |

[셋째마당 프롬프트](PROMPTS.md) · [저장소 처음으로](../README.md)
