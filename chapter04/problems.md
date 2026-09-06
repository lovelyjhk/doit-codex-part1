# 4장 마무리 문제

달빛책방은 강아지 캐릭터가 책을 소개하는 가상 책방입니다. 콘텐츠 제작 준비에 필요한 절차를 스킬로 만들어 봅니다. 모든 입력은 교육용으로 만든 가상 자료입니다.

빈 연습 폴더 `moonlight_skill_practice`를 만들고 [시작 자료](problem_start/moonlight_bookshop/)의 파일을 복사한 뒤 VS Code로 엽니다. 스킬은 `.agents/skills/<스킬이름>/SKILL.md`에 저장하고 검토한 뒤 새 대화에서 호출합니다. [입력할 프롬프트](problem_start/moonlight_bookshop/prompts.md)를 참고하세요.

## 문제 1

**문제 제목:** 1. 달빛책방 콘텐츠 제작 계약서 초안 작성 절차를 스킬로 등록하기 ★★

**문제 내용:** 의뢰서와 양식으로 검토용 초안을 만드는 절차를 스킬로 등록합니다. 입력·출력·작성 순서·금지 사항·완료 기준을 포함하고, 당사자·금액·납품일은 실행 입력에서 가져오세요. 자료에 없는 조건은 [확인 필요]로 남깁니다. 등록한 스킬을 실행해 계약서_초안.md와 계약_확인목록.md를 만들고 날짜·금액·수량·합의 상태가 원문과 일치하는지 확인하세요. 원본 양식을 보존하고 서명이나 발송은 하지 않습니다.

**필요 파일:** [콘텐츠_제작_의뢰서.md](problem_start/moonlight_bookshop/콘텐츠_제작_의뢰서.md), [계약서_양식.md](problem_start/moonlight_bookshop/계약서_양식.md)

**모범 답안 파일:** [SKILL.md](../solutions/part2/chapter04/problems/moonlight_bookshop/moonlight-contract/SKILL.md), [계약서_초안.md](../solutions/part2/chapter04/problems/moonlight_bookshop/contract/계약서_초안.md), [계약_확인목록.md](../solutions/part2/chapter04/problems/moonlight_bookshop/contract/계약_확인목록.md)

## 문제 2

**문제 제목:** 2. 달빛책방 견적서 검토 절차를 스킬로 등록하기 ★★

**문제 내용:** 의뢰서와 견적서를 비교하는 절차를 스킬로 등록합니다. 수량×단가와 합계를 검산하고 누락 작업·일정 차이·불분명한 비용을 찾으세요. 등록한 스킬을 실행해 견적서_검토.md를 만들고 검토 항목·문제 내용·확인 요청 표로 정리합니다. 원본 금액과 검산값을 구분하고 업체·수치를 스킬에 고정하지 마세요. 알 수 없는 비용은 [확인 필요]로 남기며 원본 견적서는 수정하지 않습니다.

**필요 파일:** [콘텐츠_제작_의뢰서.md](problem_start/moonlight_bookshop/콘텐츠_제작_의뢰서.md), [영상_제작_견적서.md](problem_start/moonlight_bookshop/영상_제작_견적서.md)

**모범 답안 파일:** [SKILL.md](../solutions/part2/chapter04/problems/moonlight_bookshop/moonlight-quote-review/SKILL.md), [견적서_검토.md](../solutions/part2/chapter04/problems/moonlight_bookshop/quote/견적서_검토.md)

## 문제 3

**문제 제목:** 3. 책방 영문 번역 절차를 스킬로 등록하기 ★★

**문제 내용:** 소개글과 영문 표기 기준으로 번역하는 절차를 스킬로 등록합니다. 등록한 스킬을 실행해 책방_영문번역.md와 번역_확인목록.md를 만드세요. 한국어 원문·영어 번역 표에서 이름·날짜·수치·단위를 대조하고 [확인 필요]를 유지합니다. 특정 문장·날짜를 스킬에 고정하거나 원문에 없는 설정을 추가하지 마세요. 결과는 파일로만 저장합니다.

**필요 파일:** [달빛책방_소개글.md](problem_start/moonlight_bookshop/달빛책방_소개글.md), [영문_표기_기준.md](problem_start/moonlight_bookshop/영문_표기_기준.md)

**모범 답안 파일:** [SKILL.md](../solutions/part2/chapter04/problems/moonlight_bookshop/moonlight-translate/SKILL.md), [책방_영문번역.md](../solutions/part2/chapter04/problems/moonlight_bookshop/translation/책방_영문번역.md), [번역_확인목록.md](../solutions/part2/chapter04/problems/moonlight_bookshop/translation/번역_확인목록.md)

[모범 답안 안내](../solutions/part2/chapter04/problems.md)
