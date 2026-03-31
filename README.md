## MOOC 학습자 참여 및 이탈 구조 분석
1. 프로젝트 개요

본 프로젝트는 MOOC(Massive Open Online Course) 환경에서 학습자의 참여(engagement)와 이탈(dropout) 구조를 행동 데이터 기반으로 분석하는 것을 목표로 한다.

Kaggle의 Online Course Student Engagement Metrics 데이터를 활용하였으며,
HarvardX · MITx 초기 edX 연구 맥락을 참고하여 변수의 의미를 해석하였다.

단순히 이탈 여부를 예측하는 것이 아니라,
학습자의 행동 흐름을 단계별 퍼널 구조로 정의하고,
각 단계에서 이탈이 발생하는 원인을 통계적으로 분석하였다.

2. 팀 구성
김규열
김재천
서윤범
이예린
김규리

3. 프로젝트 목표
학습자의 이탈을 단일 지표가 아닌 Stage(단계) + Duration(시간) 구조로 분해
행동 데이터 기반으로 학습 참여 패턴을 정량적으로 해석
각 단계별 전환에 영향을 주는 핵심 변수 도출
실무적으로 활용 가능한 임계값(threshold) 제시

4. 데이터 소개
Dataset: Kaggle Online Course Student Engagement Metrics
주요 변수:
registered, viewed, explored, certified
nevents, ndays_act, nplay_video, nchapters
start_time_DI, last_event_DI

본 데이터는 실제 edX 데이터 구조와 유사하며,
특히 학습 단계 변수(viewed, explored 등)가 포함되어 있어
퍼널 분석에 적합한 형태를 가진다.

5. 분석 프레임워크
5.1 Funnel 구조
본 프로젝트에서는 학습자의 행동 흐름을 다음과 같이 정의하였다:

Registered → Viewed → Explored → Sufficient
Certified는 행동 단계가 아닌 결과 변수로 판단하여 퍼널에서 제외
5.2 분석 축

본 분석은 두 가지 축으로 구성된다:

Stage (구조적 전환)
→ 학습자가 어느 단계에서 이탈하는가
Duration (시간적 이탈)
→ 얼마나 빠르게 이탈하는가 (초기 이탈: 14일 기준)

6. 분석 방법
6.1 통계적 검정
Chi-square test
Mann–Whitney U test
6.2 효과 크기 (Effect Size)
Cramér’s V
Rank-biserial correlation / Cliff’s Delta
-> 단순 p-value가 아닌 실제 영향력까지 함께 평가

6.3 임계값(Threshold) 도출
Early stage: ROC 기반
Mid stage: Precision-Recall (F1) 기반
Late stage: ROC 기반
-> 단순 최적화가 아니라
카이제곱 검정 + 효과크기로 검증된 기준

7. 주요 분석 결과
7.1 퍼널 전환율
Registered → Viewed: 약 60%
Viewed → Explored: 약 11%
Explored → Sufficient: 약 31%
-> 가장 큰 이탈 구간: Viewed → Explored

7.2 주요 행동 변수
ndays_act (활동 지속성)
nevents (총 활동량)
nplay_video (영상 소비량)
-> 특히 **활동 일수(ndays_act)**가
초기 및 중간 단계에서 가장 중요한 변수로 확인됨

7.3 초기 이탈 (Duration)
14일 이하를 초기 이탈로 정의
실제 데이터에서 대부분의 이탈이 초기에 집중됨
7.4 특이 집단 발견
"Unknown" 국가 그룹:
매우 낮은 참여율
활동 데이터 거의 없음
-> 단순 국가 정보가 아닌 저의도 사용자 또는 데이터 수집 이슈 가능성

8. Tableau 대시보드
본 프로젝트는 분석 결과를 기반으로
Tableau를 활용한 대시보드를 구축하였다.

퍼널 전환율 시각화
단계별 이탈 분석
행동 변수 분포 비교
초기 이탈 패턴 분석
-> 데이터 기반 의사결정을 위한 실무형 시각화 제공

9. 프로젝트 한계
데이터가 실제 로그가 아닌 합성 데이터일 가능성
행동 변수 간 정의 불일치 (heterogeneous logging)
인과 관계가 아닌 연관 관계 분석

10. 향후 개선 방향
A/B 테스트를 통한 인과 검증
실제 로그 데이터 적용
개인화 추천 시스템과 연계
Early intervention 전략 설계

11. 기술 스택
Python (Pandas, NumPy, SciPy, Scikit-learn)
Jupyter Notebook
Tableau
Git / GitHub