# Tableau 대시보드 KPI & Metric 정의서

> **분석 기반:** `ConfirmatoryDA.ipynb` (Duration 기반 생존 분석) + `교육EDA검정.ipynb` (PR 기반 Threshold)  
> **대상:** viewed = 1 (강의 열람자) 대상 explored 전환 관리  
> **작성일:** 2026-03-25

---
> #### 단순 AI가 작성한 예시로 참고용입니다

---
## Dashboard 1: Duration 기반 초기 이탈자 감지 및 관리

> **목적:** 가입 후 조기(Day 0~30) 이탈 위험을 실시간 모니터링하고, 고위험 사용자를 조기에 식별

### 핵심 KPI (상단 스코어카드)

| KPI | 산식 | 의미 |
|---|---|---|
| **종합 Explored 전환율** | explored = 1 / viewed = 1 | 전체 열람자 대비 탐색 전환 비율 (베이스라인) |
| **Day-3 생존율** | (duration ≥ 3인 viewed 수) / 전체 viewed 수 | Day 3까지 잔존하는 비율 |
| **조기 이탈률** | (duration ≤ 3인 이탈자) / 전체 이탈자 | 전체 이탈 중 Day 0~3의 비중 (현재 57%) |
| **Death Valley 이탈률** | (duration 4~30에서 미전환) / viewed | 중기 이탈 집중 구간 규모 |

### 세부 Metric

**퍼널 그래프** ← 대시보드 최상단 배치
- Registered → Viewed → Explored 단계별 인원수 및 전환율
- 각 단계 이탈 비율 강조 (dropped %)

**시간 기반 생존 분석**
- `duration` 구간별 조건부 전환율 (`cond_prob = explored / survivors at day X`)
- 이탈 급락 구간 히트맵 (Day 단위)

**행동 지표 모니터링**
- `ndays_act = 0`인 사용자 비율 (완전 비활성)
- `nplay_video = 0`인 사용자 비율
- `nforum_posts = 0`인 사용자 비율

**필터 / 드릴다운**
- Course ID별, 기간별, 지역(country)별 슬라이서

---

## Dashboard 2: Threshold 기반 중기 이탈자 관리선 제시

> **목적:** Precision-Recall 분석 기반 행동 임계치를 시각화하고, 사용자를 "위험/관리/안전" 구간으로 구분

### 핵심 KPI (상단 스코어카드)

| KPI | 산식 | 의미 |
|---|---|---|
| **7일 활동 달성률** | ndays_act ≥ 7인 사용자 / 전체 viewed | Tipping Point 달성 비율 |
| **Explored 전환율** | explored = 1 / viewed = 1 | 핵심 성과 지표 (현재 11.55%) |
| **F1-Score@Threshold** | 2 × (Precision × Recall) / (Precision + Recall) | 임계치 선정의 1차 기준 — 정밀도·재현율의 균형점 최적화 |
| **Recall@Threshold** | 실제 전환자 중 모델이 탐지한 비율 | 임계치 선정의 2차 기준 — 비영리 목적상 미탐지 전환자를 최소화하는 것이 우선 |

### 세부 Metric

**Threshold 관리선 시각화**
- `ndays_act` 구간별 explored 전환율 (X축: 활동일, Y축: 전환율) → Tipping Point(7일) 표시선 포함
- `nevents` 구간별 전환율 (분위수 기준)
- `nplay_video` 구간별 전환율

**사용자 구간 분류 (3-Zone)**
- 🔴 위험 구간: `ndays_act ≤ 3` 사용자 수 및 비율
- 🟡 관리 구간: `ndays_act 4~6` 사용자 수 및 비율
- 🟢 안전 구간: `ndays_act ≥ 7` 사용자 수 및 비율

**PR 커브 기반 지표**
- Precision-Recall Curve (각 ndays_act 임계치마다 P/R 값 플롯)
- F1-Score 최대 지점 강조 (최적 Threshold)
- 임계치 변화에 따른 전환율 변화량

**행동 조합 분석**
- `ndays_act × nplay_video` 조합별 전환율 히트맵
- `ndays_act × nevents` 조합별 전환율 히트맵
- 포럼 참여 여부(nforum_posts > 0)에 따른 전환율 차이

**개입 효과 추정**
- 각 Zone의 사용자가 다음 Zone으로 이동 시 예상 추가 전환자 수 (What-if 파라미터)

---

## 공통 고려사항

| 항목 | 권장 사항 |
|---|---|
| 데이터 갱신 | 주간 스냅샷 기준 (배치) |
| 기준 필터 | `viewed = 1` 조건 필수 고정 |
| 비교 기준선 | 전체 베이스라인(11.55%)을 모든 차트에 Reference Line으로 표시 |
| 색상 정책 | 🔴 위험 < 5%, 🟡 관리 5~11%, 🟢 안전 > 11% |
