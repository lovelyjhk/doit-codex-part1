# 넷째마당 프롬프트

넷째마당(11~14장) 본문에 나오는 프롬프트를 책과 같은 문장으로 모았습니다. 실습 순서대로 한 단계씩 입력하고, 결과 파일을 연 다음 다음 단계로 넘어갑니다.

- 먼저 [시작 안내](README.md)의 작업 규칙을 읽고, 표에 적힌 폴더를 VS Code에서 엽니다.
- `@파일명`은 입력란에 `@`를 입력한 뒤 목록에서 그 파일을 고르라는 뜻입니다. 아직 만들지 않은 결과 파일은 `@` 없이 이름만 적혀 있습니다.
- 실습의 첫 프롬프트에 있는 "너는 ○○ 도우미야." 같은 문장은 그 실습에서 코덱스가 맡을 역할입니다.
- 앞 단계에서 내가 답하거나 확인해 준 내용을 전제로 하는 프롬프트가 있습니다. 책의 설명을 함께 읽으며 입력하세요.

## 넷째마당 기본기

### 긴 작업은 CONTEXT.md로 이어 갑니다

```text
@AGENTS.md와 @CONTEXT.md를 읽어 줘. 완료한 일과 남은 일을 확인하고, 바꾸지 말아야 할 파일과 먼저 확인할 검증 절차를 정리해 줘. 외부 업로드나 실제 서비스 변경은 하지 마.
```

## 11장 국가유산포털에서 우리 동네 국가유산 찾기

### [Do it! 실습 42] 우리 지역 국가유산 5곳 근거표 만들기

VS Code에서 열 폴더: `chapter11`

#### 1. 검색할 지역과 조건을 정합니다

```text
너는 공식 상세 페이지의 값만 기록하는 자료 조사 도우미야.
@AGENTS.md와 @heritage_search/search_conditions_template.md를 읽어 지역·지정종목·시대·유형의 검색 조건을 정리해 줘. 실제로 비어 있는 조건은 질문으로 남기고 검색 결과를 미리 만들지 마.
```

#### 2. 공식 상세 페이지에서 다섯 건을 고릅니다

```text
내가 공식 상세 페이지에서 확인한 명칭·지정종목·소재지·관리자·URL·확인일만 @heritage_search/source_log.csv 사본에 기록해 줘. 서로 다른 다섯 건인지 확인하고 검색 요약이나 사진은 근거로 쓰지 마.
```

#### 3. 출처 기록으로 후보표를 만듭니다

```text
채운 @heritage_search/source_log.csv만 읽어 heritage_search/heritage_candidates.csv를 만들어 줘. 열은 국가유산명, 지정종목, 소재지, 관리자, 공식_상세_URL, 확인일_KST로 정하고 원본에 없는 값은 확인 필요로 표시해 줘.
```

#### 4. 후보표를 출처 기록과 비교합니다

```text
@heritage_search/source_log.csv와 @heritage_search/heritage_candidates.csv를 행별로 대조해 @heritage_search/verification_notes.md에 일치·차이·확인 필요를 적어 줘. URL과 확인일을 포함한 여섯 열을 비교하고 원본은 수정하지 마.
```

#### 5. 사진 이용과 사실 출처를 구분합니다

```text
@heritage_search/heritage_candidates.csv에 포털 사진이나 사진 이용 허락을 대신 판단한 문장이 없는지 확인해 줘. 출처 표기와 사진 이용 권리는 분리하고, 외부 사진을 내려받거나 결과에 넣지 마.
```

#### 6. 직접 선택한 이유를 기록하고 최종 점검합니다

```text
@heritage_search/heritage_candidates.csv가 다섯 행인지, URL·확인일과 남은 확인이 있는지 최종 점검해 줘. 내가 직접 선택한 이유만 @heritage_search/verification_notes.md에 추가하고 선택하지 않은 이유는 만들지 마.
```

### [한 걸음 더!] 공식 출처 근거표 절차를 스킬로 저장하기

```text
$skill-creator @AGENTS.md와 @heritage_search/verification_notes.md를 참고해 공식 출처 근거표 스킬을 만들어 줘.
- 스킬 이름: official-source-table
- 저장 위치: 현재 폴더의 .agents/skills/official-source-table/SKILL.md
- 순서: 공식 상세 페이지 값만 source_log에 기록 → 결과표 작성 → 원본과 행별 대조 → 근거 없는 값은 '확인 필요'
- 특정 지역·제품명·날짜는 스킬에 고정하지 않는다.
- 인증키·개인정보는 스킬과 결과에 넣지 않는다.
지금은 스킬 파일만 만들고 표 작업은 하지 마.
```

### [Do it! 실습 43] 2025 국가유산 현황에서 내 지역 숫자 검산하기

VS Code에서 열 폴더: `chapter11`

#### 1. 공식 게시물과 첨부 자료를 확인합니다

```text
너는 원본 통계와 계산값을 대조하는 데이터 검산 도우미야.
@heritage_stats/download_and_verify.md와 @heritage_stats/source_metadata.md를 읽어 원본 게시물·첨부명·기준일을 확인할 목록을 보여 줘. 아직 받지 않은 엑셀을 읽었다고 하지 말고, 내가 확인한 값만 기록해 줘.
```

#### 2. 엑셀을 내려받고 시트와 머리글을 봅니다

```text
heritage_stats/raw 폴더에서 내가 내려받은 엑셀 파일의 정확한 이름을 먼저 확인해 줘. 파일이 없으면 다운로드를 요청하고 멈춰 줘. 있으면 시트명·머리글·지역 열·분류 열·값 열·데이터 시작 행을 보여 주고 수정하지 마.
```

#### 3. 집계할 지역과 항목을 정합니다

```text
내가 지정한 지역 하나와 통계 항목 하나만 집계할 계획을 보여 줘. 사용할 정확한 원본 파일·시트·셀 범위와 빈 셀 처리 방법을 적어 주고, 승인 전에는 결과를 만들지 마.
```

#### 4. 결과표를 만들고 원본 합계와 비교합니다

```text
확인한 계획대로 heritage_stats/region_summary.csv를 만들어 줘. 분류별 값·원본 시트와 셀 범위·계산식·합계·데이터 기준일·확인일을 기록하고, 원본 합계와의 차이를 @heritage_stats/verification_log.md에 적어 줘. 빈 셀의 뜻이 불명확하면 0으로 바꾸지 마.
```

#### 5. 한 행을 직접 계산해 비교합니다

```text
원본 분류 한 행과 계산식을 보여 줘. 내가 직접 계산해 준 값과 자동 계산값을 @heritage_stats/verification_log.md에서 비교하고, 차이가 있으면 원인 추정 대신 두 값과 확인할 셀을 남겨 줘.
```

#### 6. 결과표의 기준일과 출처를 확인합니다

```text
@heritage_stats/region_summary.csv의 데이터 기준일·확인일·기관명·자료명·원문 URL을 점검해 줘. 기준일은 읽은 자료의 값만 적고 최신 현황이라고 표현하지 마. 읽지 못한 원본이나 검산하지 못한 항목은 미확인으로 남겨 줘.
```

## 12장 국가유산 자료로 쉬운 교육 콘텐츠 만들기

### [Do it! 실습 44] 한국의 세계유산 3곳을 쉬운 설명 카드로 만들기

VS Code에서 열 폴더: `chapter12`

#### 1. CSV의 열과 수집일을 읽습니다

```text
너는 원자료 범위 안에서 쉬운 문장을 쓰는 교육 콘텐츠 작가야.
@unesco_cards/source_metadata.md와 @unesco_cards/unesco_world_heritage_sample.csv를 읽어 열 이름·행 수·수집일·가상 예시 여부를 알려 줘. 샘플의 값이 현재 등재 현황인지 추정하지 마.
```

#### 2. 소개할 세 곳을 직접 고릅니다

```text
CSV에 실제 있는 행 가운데 내가 고른 세 행의 번호와 이름을 보여 줘. 선택 이유는 내가 제공한 내용만 @unesco_cards/author_choice.md 사본에 기록하고 근거 없는 이유를 만들지 마.
```

#### 3. 카드의 항목과 구성을 정합니다

```text
@unesco_cards/card_template.md를 기준으로 카드의 명칭·위치·등재연도·쉬운 설명·원문 URL·수집일 구성을 계획해 줘. 근거는 선택한 CSV 세 행으로 제한하고 아직 카드는 만들지 마.
```

#### 4. 쉬운 설명 카드 세 장을 만듭니다

```text
@unesco_cards/unesco_world_heritage_sample.csv에서 @unesco_cards/author_choice.md에 기록한 세 행만 근거로 unesco_cards/heritage_cards.md를 만들어 줘. 카드마다 쉬운 한국어 세 문장으로 설명하고 CSV에 없는 운영시간·입장료·교통·추천 표현은 추가하지 마.
```

#### 5. 카드의 문장과 원자료를 연결합니다

```text
@unesco_cards/heritage_cards.md의 사실 문장마다 CSV 행 번호와 사용한 열을 @unesco_cards/claim_source_map.csv 사본에 적어 줘. 근거가 연결되지 않는 문장은 수정 후보로 표시하고, 외부 사진이나 원문 장문 인용은 넣지 마.
```

#### 6. 공식 페이지의 명칭을 다시 비교합니다

```text
내가 공식 상세 페이지에서 확인한 최신 명칭만 @unesco_cards/heritage_cards.md의 명칭과 대조해 줘. 차이가 있으면 어느 쪽이 최신인지 추정하지 말고 두 표기·URL·확인일을 unesco_cards/name_recheck.md에 남겨 줘.
```

### [Do it! 실습 45] 공식 자료로 6장 국가유산 교육용 PPT 만들기

VS Code에서 열 폴더: `chapter12`

#### 1. PPT 여섯 장의 구성을 정합니다

```text
너는 출처가 보이는 교육용 발표 자료를 만드는 PPT 기획자야.
@heritage_deck/CONTEXT.md와 @heritage_deck/source_cards.csv를 읽어 PPT 여섯 장의 역할을 계획해 줘. 제목, 자료 확인 방법, 카드 세 장, 확인 필요와 출처 순서로 제안하고 파일은 아직 만들지 마.
```

#### 2. 슬라이드에 넣을 핵심 문장을 고릅니다

```text
내가 @heritage_deck/source_cards.csv에서 고른 핵심 문장만 heritage_deck/deck_outline.md에 정리해 줘. 각 슬라이드는 한 메시지로 하고 자료에 없는 사실·추천·사진은 추가하지 마.
```

#### 3. 계획대로 PPT 파일을 만듭니다

```text
확인한 구성대로 heritage_deck/heritage_class_author.pptx를 만들어 줘. 16:9·밝은 배경·큰 글자·슬라이드당 한 메시지를 적용하고 3~5장에 원문 URL과 수집일을 표시해 줘. 6장에는 출처와 재확인 항목을 넣고 제공된 예제 PPT는 덮어쓰지 마.
```

#### 4. 슬라이드를 이미지로 내보내 확인합니다

```text
@heritage_deck/heritage_class_author.pptx 여섯 장을 heritage_deck/output/render 폴더에 이미지로 내보내 줘. 렌더링할 수 없으면 그 이유와 직접 확인할 방법을 알려 주고, 실행하지 않은 렌더 검사를 통과로 기록하지 마.
```

#### 5. PPT의 사실과 화면을 점검합니다

```text
@heritage_deck/source_cards.csv와 PPT의 숫자·명칭·URL·수집일을 대조하고 렌더 이미지의 잘림·겹침·작은 글자를 heritage_deck/deck_qa_report_author.md에 기록해 줘. 확인하지 못한 항목은 미확인으로 남겨 줘.
```

#### 6. 직접 다듬은 문장을 반영합니다

```text
내가 수정한 도입 문장과 마무리 질문만 PPT에 반영하고 @heritage_deck/author_revision_log.md 사본에 수정 전후와 이유를 적어 줘. 사실 자료·출처 문구·제공된 예제는 바꾸지 마.
```

## 13장 식품안전나라에서 제품과 위험 신호 확인하기

### [Do it! 실습 46] 포장 식품 한건의 제품 정보와 회수 여부 확인표 만들기

VS Code에서 열 폴더: `chapter13`

#### 1. 제품 포장의 식별 정보를 적습니다

```text
너는 제품 식별 정보와 공식 기록을 대조하는 확인 도우미야.
@product_recall/product_identity_template.md를 복사해 내가 확인한 제품명·제조업체·품목보고번호 또는 바코드·소비기한만 product_recall/product_identity.md에 적어 줘. 입력하지 않은 식별자는 확인 필요로 남기고 개인정보는 기록하지 마.
```

#### 2. 공식 국내식품 등록 정보를 찾습니다

```text
@product_recall/product_identity.md를 읽어 국내식품 검색에 사용할 검색어와 대조할 식별자를 보여 줘. 내가 공식 페이지에서 확인한 URL·값·확인일만 @product_recall/search_log.csv 사본에 기록해 줘.
```

#### 3. 회수·판매중지 정보를 따로 검색합니다

```text
회수·판매중지 정보는 국내식품 등록과 별도로 확인할 목록을 보여 줘. 내가 확인한 공식 검색 결과만 @product_recall/search_log.csv 사본에 추가하고, 검색 결과 없음을 안전 인증으로 표현하지 마.
```

#### 4. 제품 정보와 검색 기록을 비교합니다

```text
@product_recall/product_identity.md와 @product_recall/search_log.csv를 근거로 product_recall/output/product_recall_check.md를 만들어 줘. 제품명·제조업체·보고번호 또는 바코드·소비기한을 나란히 적고 결론은 일치·불일치·판단 보류 중 하나만 사용해 줘.
```

#### 5. 결론에 사용한 식별 정보를 확인합니다

```text
@product_recall/output/product_recall_check.md에서 결론의 근거 식별자를 다시 점검해 줘. 식별 정보가 부족하면 판단 보류로 남기고, 제품명이 같다는 이유만으로 일치라고 하지 마. 섭취·진단·치료·구매 조언은 하지 마.
```

#### 6. 공식 안내 위치와 남은 질문을 기록합니다

```text
공식 URL·확인일시·남은 질문과 공식 페이지의 안내 위치를 @product_recall/output/product_recall_check.md에 추가해 줘. 내가 직접 확인하지 않은 반품 지침이나 상담 결과는 만들지 말고 @human_approval_checkpoint.md의 확인 지점에서 멈춰 줘.
```

### [Do it! 실습 47] 해외직구 제품·성분 차단 정보 확인표 만들기

VS Code에서 열 폴더: `chapter13`

#### 1. 제품과 성분 정보를 정리합니다

```text
너는 해외직구 제품의 공식 검색 기록을 정리하는 확인 도우미야.
@direct_import/direct_purchase_input_template.md를 복사해 내가 입력한 제품명·제조사·제조국가·성분명만 direct_import/purchase_input.md에 적어 줘. 계정·주문번호·결제정보는 입력 항목에 넣지 마.
```

#### 2. 공식 화면에서 사용할 검색어를 나눕니다

```text
@direct_import/purchase_input.md에서 제품·원료·성분 검색에 쓸 검색어를 구분해 보여 줘. 공식 화면에서 내가 확인한 탭 이름과 입력 규칙만 사용하고 현재 화면을 보지 못했으면 확인 필요로 남겨 줘.
```

#### 3. 제품명과 성분명으로 따로 검색합니다

```text
내가 제품명과 성분명으로 따로 확인한 공식 검색 결과·건수·URL·확인일만 @direct_import/search_log.csv 사본에 기록해 줘. 검색하지 않은 항목을 검색 결과 없음으로 적지 마.
```

#### 4. 제품 정보와 공식 상세 값을 비교합니다

```text
@direct_import/purchase_input.md와 @direct_import/search_log.csv만 근거로 direct_import/direct_import_check.md를 만들어 줘. 제조국가·제조사·검출성분·등록일·공식 상세 URL을 대조하고 부족한 정보는 확인 필요로 표시해 줘.
```

#### 5. 검색 범위에 맞는 결론을 기록합니다

```text
@direct_import/direct_import_check.md의 검사 결과는 차단 목록 일치·검색 결과 없음·판단 보류로 구분해 줘. 검색 결과 없음은 확인 시점에 해당 검색어로 기록을 찾지 못했다는 뜻으로만 설명하고 섭취 안전이나 구매 추천으로 바꾸지 마.
```

#### 6. 다시 확인할 질문을 만듭니다

```text
같은 상품의 국가·버전·성분·최신 등록 상태를 다시 확인할 질문 세 개를 direct_import/recheck_questions.md에 적어 줘. 근거 URL과 확인일을 남기고 주문·로그인·결제는 하지 마.
```

## 14장 식품안전 OpenAPI와 유해물질 기준 읽기

### [한 걸음 더!] 보조 에이전트로 읽기 검수 나누기

```text
@subagent_task_cards.md의 역할 A·B·C를 서브에이전트 세 개에 하나씩 맡겨 줘. 각 서브에이전트는 카드에 적힌 파일만 읽고 결과 파일 하나만 만든다. 세 결과가 모두 돌아오면 서로 다른 점을 충돌표로 정리해 줘. 최종 카드 문장은 내가 정한다.
```

> 이지스팁: 두 코덱스를 병행할 때는 같은 원고를 동시에 고치지 않습니다.

```text
@HANDOFF_TEMPLATE.md를 기준으로 코덱스 A와 B의 담당 파일을 겹치지 않게 나눠 줘. 각 코덱스는 자기 결과 파일만 만들고 인수인계 문서의 상태를 갱신한다. 두 결과가 끝나면 원본과 대조한 충돌표를 만들되 최종 병합은 한 작업에서만 수행해.
```

### [Do it! 실습 48] 회수·판매중지 샘플 XML을 CSV로 변환하기

VS Code에서 열 폴더: `chapter14`

#### 1. 샘플의 출처와 파일 해시를 확인합니다

```text
너는 XML 샘플을 원문 그대로 CSV로 옮기는 데이터 변환 도우미야.
@recall_api/source_metadata.json과 @recall_api/raw/recall_sample.xml을 읽어 서비스 ID·URL·수집일·is_sample과 파일의 실제 SHA-256을 비교해 줘. 기록과 다른 값은 @reproducibility_log.md 사본에 남기고 원본은 수정하지 마.
```

#### 2. XML의 태그와 제품 행 수를 읽습니다

```text
@recall_api/raw/recall_sample.xml에서 실제 제품 행을 나타내는 요소와 제품명·회수사유·제조업체·바코드·소비기한·등록일의 태그를 보여 줘. total_count와 이번 샘플 행 수를 구분하고 아직 CSV를 만들지 마.
```

#### 3. 샘플 다섯 건을 CSV로 바꿉니다

```text
계획대로 샘플 다섯 건을 recall_api/output/recall_sample_author.csv로 변환해 줘. 열은 product_name,recall_reason,manufacturer,barcode,expiry_or_use_by,registration_date,source_url,retrieved_at_kst,is_sample 순서로 하고 원문 값은 고치지 마. 마지막 세 열은 @recall_api/source_metadata.json의 근거로 채우고 is_sample=true로 표시해 줘.
```

#### 4. 빈 값과 식별자가 유지되었는지 봅니다

```text
@recall_api/output/recall_sample_author.csv의 빈 값과 식별자 문자열이 @recall_api/raw/recall_sample.xml의 원문과 같은지 확인해 줘. 없는 값을 0·미상·추정 바코드로 채우지 말고, 원문에서 빈 값인 필드는 빈칸으로 유지해 줘.
```

#### 5. 첫 제품을 XML과 CSV에서 비교합니다

```text
@recall_api/raw/recall_sample.xml의 첫 제품과 @recall_api/output/recall_sample_author.csv의 첫 행에서 제품명·제조업체·회수사유·등록일을 필드별로 비교해 recall_api/output/api_verification_log_author.md에 일치 여부를 기록해 줘. 행 수 다섯 건과 열 순서도 확인해 줘.
```

#### 6. 샘플 표시와 실행 과정을 기록합니다

```text
CSV의 모든 행에 is_sample=true가 있는지 확인하고 @reproducibility_log.md 사본에 입력 해시·서비스 ID·URL·수집일·행 수·실행 방법을 기록해 줘. 이 결과를 현재 회수 목록으로 표현하지 마.
```

### [Do it! 실습 49] 유해물질 기준·규격 한 행을 바탕으로 안전 여부를 단정하지 않는 설명 카드 만들기

VS Code에서 열 폴더: `chapter14`

#### 1. 제공 자료의 서비스 ID와 출처를 읽습니다

```text
너는 기준·규격 원문을 옮겨 적는 자료 정리 도우미야.
@hazard_standard/source_metadata.json을 읽어 서비스 ID·원문 URL·수집일을 보여 줘. 공식 서비스명은 내가 확인한 자료와만 대조하고 이름의 연결 관계를 추정하지 마.
```

#### 2. XML 첫 행의 태그와 값을 봅니다

```text
@hazard_standard/raw/hazard_sample.xml의 첫 row만 읽어 원문 태그와 값을 표로 보여 줘. 품목명·시험항목·세부항목·기준규격값·유효개시일·유효종료일·판정형식·단위를 임의로 보완하지 마.
```

#### 3. 원문을 옮긴 설명 카드를 만듭니다

```text
@hazard_standard/raw/hazard_sample.xml의 첫 row와 @hazard_standard/no_judgment_card_template.md만 근거로 hazard_standard/hazard_standard_card.md를 만들어 줘. 원문 태그·값·필드 역할을 나란히 적고 카드 맨 위에 이 자료만으로 특정 제품이나 개인의 섭취 안전성을 판단할 수 없다고 써 줘. 허용 섭취량·질병 위험·제품 적합 여부는 계산하거나 단정하지 마.
```

#### 4. 빈 정보와 모호한 항목을 질문으로 남깁니다

```text
@hazard_standard/hazard_standard_card.md에서 단위·시험법·유효기간·식품 분류가 비거나 모호한 항목을 @hazard_standard/confirmation_log.md 사본의 전문가 확인 필요 칸에 이유와 함께 적어 줘. 빈 정보를 추정하지 마.
```

#### 5. 종료일 값의 뜻을 확인할 질문을 적습니다

```text
@hazard_standard/hazard_standard_card.md에 옮긴 유효종료일 값을 원문 그대로 유지하고 99991231 같은 값이 영구 유효를 뜻하는지 단정하지 마. 시스템 값의 설명을 공식 기관에 확인할 질문으로 남겨 줘.
```

#### 6. 카드를 원문과 대조합니다

```text
@hazard_standard/raw/hazard_sample.xml의 첫 row와 @hazard_standard/hazard_standard_card.md의 모든 값을 대조하고 불일치·누락·안전 단정 표현을 @hazard_standard/confirmation_log.md 사본에 기록해 줘. 표의 원문 값은 고치지 말고 카드에서 현재 제품이나 개인에 대한 안전 판정을 내리지 마.
```

[시작 안내](README.md) · [저장소 처음으로](../README.md)
