Starbucks Promotion Data Analysis – Data Limitation Study
1. Overview

This project analyzes Starbucks promotion data with the goal of evaluating promotion effectiveness.
During the analysis, critical structural issues were identified in the dataset, leading to a reassessment of the analysis approach.

2. Key Problem

The main issue lies in the transaction data:

The amount in transactions cannot be attributed to a specific promotion
It is impossible to distinguish:
promotion-driven purchases vs.
regular customer purchases

-> As a result, promotion-driven revenue cannot be reliably measured

3. Core Findings
Transactions within promotion periods are not causally linked to promotions
Some cases show:
promotion conditions met (difficulty satisfied)
but no offer completed event
Completion timing is often inconsistent with transaction timing

-> This indicates a disconnect between transaction data and promotion logic

4. Impact on Analysis

Using transaction-based KPIs leads to:

- Overestimation (including unrelated purchases)
- Underestimation (missing completion events)

-> Therefore, revenue-based KPI design is unreliable

5. KPI Design Attempts

Several alternative approaches were explored:

Using difficulty & reward as proxy metrics
Applying weights (α, β) for estimated effects
Funnel-based metrics (received → viewed → completed)

However:

BOGO-type offers → difficulty = reward → no meaningful margin
Weighting lacked objective justification
No proper control group for causal analysis

-> All approaches faced structural limitations

6. Conclusion
This dataset is suitable for:
- behavioral analysis (viewed, completed)
But not suitable for:
- attribution-based analysis
- causal inference

-> Therefore, this project concludes that:

The dataset has structural limitations and is not appropriate for reliable KPI design.
Further analysis should be conducted using a dataset with clearer attribution structure.