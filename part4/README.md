# 넷째마당 · 에이전트 기반의 코덱스 사용하기

넷째마당은 11~14장입니다. 국가유산·식품안전 공공데이터와 공식 자료를 근거로 표·소개 카드·PPT·CSV를 만들고, 스킬·/goal·서브에이전트로 반복 작업과 긴 작업을 다루는 방법을 연습합니다.

## 이 순서로 시작하세요

1. 저장소의 **Code → Download ZIP**으로 자료를 내려받고 압축을 풉니다.
2. 아래 표에서 실습의 장 폴더(`chapter11`~`chapter14`)를 작업할 위치에 복사합니다. 내려받은 원래 폴더는 그대로 보관합니다.
3. VS Code의 [파일 → 폴더 열기]로 복사한 장 폴더를 엽니다. 각 장 폴더의 `AGENTS.md`에 이 마당에서 지킬 작업 규칙이 들어 있습니다.
4. [넷째마당 프롬프트](PROMPTS.md)에서 해당 실습의 프롬프트를 단계 순서대로 입력합니다.
5. 마무리 문제를 푼 뒤 모범 답안과 비교합니다.

## 작업 규칙

- 책의 파일 경로는 VS Code에서 연 장 폴더를 기준으로 씁니다. 슬래시(/) 앞은 폴더, 뒤는 파일 이름입니다.
- 프롬프트의 `@파일명`은 입력란에 `@`를 입력한 뒤 목록에서 그 파일을 고르라는 뜻입니다. 아직 만들지 않은 결과 파일은 `@` 없이 이름만 적습니다.
- 실습의 첫 프롬프트에 있는 "너는 ○○ 도우미야."는 그 실습에서 코덱스가 맡을 역할입니다.
- 공식 상세 페이지와 제공 파일을 먼저 확인합니다. 검색 요약문은 후보를 찾는 데만 쓰고, 결과에는 출처 URL·데이터 기준일·확인일을 남깁니다.
- `raw` 폴더의 원본 파일은 수정하지 않습니다. 근거가 없는 값은 추정하지 않고 확인 필요로 남깁니다.
- 식품·유해물질 자료로 안전·진단·치료를 판단하지 않습니다. 검색 결과 없음은 안전하다는 뜻이 아닙니다.
- 14장 실습에는 인증 키가 필요 없습니다. 실시간 API를 따로 연습할 때도 인증 키를 프롬프트·파일·캡처에 넣지 않습니다.

## 함께 쓰는 파일

| 용도 | 파일 | 책의 위치 |
|---|---|---|
| 새 대화에서 이어 가기 | [CONTEXT_template.md](../chapter11/CONTEXT_template.md)를 작업 폴더에 복사해 `CONTEXT.md`로 저장 | 넷째마당 기본기 |
| 공식 출처 근거표 스킬 | [모범 답안 SKILL.md](../chapter11/answers/official-source-table/SKILL.md). 다른 장에서 쓰려면 `.agents` 폴더를 그 장 폴더에 복사 | 11장 한 걸음 더!, 13장 |
| /goal 사용 안내 | [GOAL_사용법.md](../chapter14/GOAL_사용법.md) | 14장 |
| 서브에이전트 검수 카드 | [subagent_task_cards.md](../chapter14/subagent_task_cards.md). 실습 48·49를 마친 뒤 사용 | 14장 한 걸음 더! |
| 인수인계 양식 | [HANDOFF_TEMPLATE.md](../chapter14/HANDOFF_TEMPLATE.md) | 14장 |

## 본문 실습

| 장 | 실습 | VS Code에서 열 폴더 | 시작 파일 | 프롬프트 |
|---|---|---|---|---|
| 11장 | 실습 42 우리 지역 국가유산 5곳 근거표 만들기 | [`chapter11`](../chapter11/) | [AGENTS.md](../chapter11/AGENTS.md), [CONTEXT_template.md](../chapter11/CONTEXT_template.md), [search_conditions_template.md](../chapter11/heritage_search/search_conditions_template.md), [source_log.csv](../chapter11/heritage_search/source_log.csv) | [보기](PROMPTS.md#do-it-실습-42-우리-지역-국가유산-5곳-근거표-만들기) |
| 11장 | 실습 43 2025 국가유산 현황에서 내 지역 숫자 검산하기 | [`chapter11`](../chapter11/) | [download_and_verify.md](../chapter11/heritage_stats/download_and_verify.md), [source_metadata.md](../chapter11/heritage_stats/source_metadata.md), [region_summary_template.csv](../chapter11/heritage_stats/region_summary_template.csv) | [보기](PROMPTS.md#do-it-실습-43-2025-국가유산-현황에서-내-지역-숫자-검산하기) |
| 12장 | 실습 44 한국의 세계유산 3곳을 쉬운 설명 카드로 만들기 | [`chapter12`](../chapter12/) | [unesco_world_heritage_sample.csv](../chapter12/unesco_cards/unesco_world_heritage_sample.csv), [source_metadata.md](../chapter12/unesco_cards/source_metadata.md), [card_template.md](../chapter12/unesco_cards/card_template.md) | [보기](PROMPTS.md#do-it-실습-44-한국의-세계유산-3곳을-쉬운-설명-카드로-만들기) |
| 12장 | 실습 45 공식 자료로 6장 국가유산 교육용 PPT 만들기 | [`chapter12`](../chapter12/) | [CONTEXT.md](../chapter12/heritage_deck/CONTEXT.md), [source_cards.csv](../chapter12/heritage_deck/source_cards.csv), [deck_outline_template.md](../chapter12/heritage_deck/deck_outline_template.md) | [보기](PROMPTS.md#do-it-실습-45-공식-자료로-6장-국가유산-교육용-ppt-만들기) |
| 13장 | 실습 46 포장 식품 한건의 제품 정보와 회수 여부 확인표 만들기 | [`chapter13`](../chapter13/) | [agent_work_cycle.md](../chapter13/agent_work_cycle.md), [human_approval_checkpoint.md](../chapter13/human_approval_checkpoint.md), [product_identity_template.md](../chapter13/product_recall/product_identity_template.md), [search_log.csv](../chapter13/product_recall/search_log.csv) | [보기](PROMPTS.md#do-it-실습-46-포장-식품-한건의-제품-정보와-회수-여부-확인표-만들기) |
| 13장 | 실습 47 해외직구 제품·성분 차단 정보 확인표 만들기 | [`chapter13`](../chapter13/) | [direct_purchase_input_template.md](../chapter13/direct_import/direct_purchase_input_template.md), [search_log.csv](../chapter13/direct_import/search_log.csv) | [보기](PROMPTS.md#do-it-실습-47-해외직구-제품성분-차단-정보-확인표-만들기) |
| 14장 | 실습 48 회수·판매중지 샘플 XML을 CSV로 변환하기 | [`chapter14`](../chapter14/) | [source_metadata.json](../chapter14/recall_api/source_metadata.json), [recall_sample.xml](../chapter14/recall_api/raw/recall_sample.xml), [expected_columns.md](../chapter14/recall_api/expected_columns.md) | [보기](PROMPTS.md#do-it-실습-48-회수판매중지-샘플-xml을-csv로-변환하기) |
| 14장 | 실습 49 유해물질 기준·규격 한 행을 바탕으로 안전 여부를 단정하지 않는 설명 카드 만들기 | [`chapter14`](../chapter14/) | [source_metadata.json](../chapter14/hazard_standard/source_metadata.json), [hazard_sample.xml](../chapter14/hazard_standard/raw/hazard_sample.xml), [no_judgment_card_template.md](../chapter14/hazard_standard/no_judgment_card_template.md) | [보기](PROMPTS.md#do-it-실습-49-유해물질-기준규격-한-행을-바탕으로-안전-여부를-단정하지-않는-설명-카드-만들기) |

11장 실습 43의 통계 엑셀은 재배포하지 않습니다. [다운로드 안내](../chapter11/heritage_stats/download_and_verify.md)에 따라 공식 게시물에서 직접 내려받아 `heritage_stats/raw` 폴더에 넣습니다.

## 마무리 문제

| 장 | 마무리 문제 | 실습 파일 | 모범 답안 |
|---|---|---|---|
| 11장 | 1. 국가유산 공식 근거표 만들기 ★ | [search_conditions_template.md](../chapter11/heritage_search/search_conditions_template.md) | [chapter11_practice_answers.md](../chapter11/answers/chapter11_practice_answers.md) |
| 11장 | 2. 통계 기준일과 합계를 검산하기 ★★ | [region_summary_template.csv](../chapter11/heritage_stats/region_summary_template.csv) | [chapter11_practice_answers.md](../chapter11/answers/chapter11_practice_answers.md) |
| 12장 | 1. 문장별 근거가 있는 소개 카드 만들기 ★ | [unesco_world_heritage_sample.csv](../chapter12/unesco_cards/unesco_world_heritage_sample.csv) | [chapter12_practice_answers.md](../chapter12/answers/chapter12_practice_answers.md) |
| 12장 | 2. 교육용 PPT 사실 검수표 만들기 ★★ | [source_cards.csv](../chapter12/heritage_deck/source_cards.csv) | [chapter12_practice_answers.md](../chapter12/answers/chapter12_practice_answers.md) |
| 13장 | 1. 제품 식별 정보와 회수 기록 대조표 만들기 ★ | [product_identity_template.md](../chapter13/product_recall/product_identity_template.md) | [chapter13_practice_answers.md](../chapter13/answers/chapter13_practice_answers.md) |
| 13장 | 2. 해외직구 제품 검색 기록 만들기 ★★ | [direct_purchase_input_template.md](../chapter13/direct_import/direct_purchase_input_template.md) | [chapter13_practice_answers.md](../chapter13/answers/chapter13_practice_answers.md) |
| 14장 | 1. 회수 샘플 XML 변환 결과 검증하기 ★ | [recall_sample.xml](../chapter14/recall_api/raw/recall_sample.xml) | [chapter14_practice_answers.md](../chapter14/answers/chapter14_practice_answers.md) |
| 14장 | 2. 유해물질 기준 판단 금지 카드 만들기 ★★ | [hazard_sample.xml](../chapter14/hazard_standard/raw/hazard_sample.xml) | [chapter14_practice_answers.md](../chapter14/answers/chapter14_practice_answers.md) |

[넷째마당 프롬프트](PROMPTS.md) · [저장소 처음으로](../README.md)
