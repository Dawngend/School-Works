# StatAna (CS0073) Summative 2: Actual Questions (Modules 3 and 4)

Taken Wed Oct 7, 2026, 11 AM. 21 questions total; Dawn pasted the first 10 below. Use these as the STYLE reference
for future StatAna reviewers and practice decks.

**Style:** scenario-based, applied judgment questions (a business situation, then "what is the strongest critique /
best response / what should be monitored"). Not slide-literal recall. The right answer is usually the most complete,
balanced, practice-minded option; wrong options are absolutes ("always", "only", "proves", "automatically").

1. A customer churn model has 95% accuracy while only 5% churn. Strongest critique?
   **Answer:** Accuracy may equal the majority baseline, so minority-class metrics and decision costs are needed.
2. A model is retrained after customer behavior changes substantially. What should be monitored?
   **Answer:** Data drift, target drift, subgroup performance, and whether the model still meets acceptance criteria.
3. A team uses all available data to tune and report the final model score. Principal limitation?
   **Answer:** The score may be optimistic because the same information influenced fitting and evaluation.
4. The lowest-RMSE model violates a fairness constraint. Best response?
   **Answer:** Treat fairness and operational constraints as acceptance criteria alongside predictive error.
5. A coefficient changes a lot when a related predictor is removed, but predictions barely change. Interpretation?
   **Answer:** Shared information may make individual coefficients unstable while aggregate predictions remain robust.
6. A business objective says "build the most accurate model". Why incomplete?
   **Answer:** It should specify the decision, forecast horizon, acceptable errors, constraints, and deployment context.
7. A model is accurate on average but consistently overpredicts low-volume stores. What should be reported?
   **Answer:** Segment-level calibration and residual patterns, together with possible weighting or model redesign.
8. A report has a significant p-value but omits sample size, effect estimate, and interval. Best improvement?
   **Answer:** Report the estimate, uncertainty, sample context, assumptions, and practical meaning alongside significance.
9. A model is used for a high-stakes decision. Strongest validation practice?
   **Answer:** Test on representative unseen data, inspect subgroup errors, document limitations, and monitor after deployment.
10. Predict monthly demand, then choose inventory levels. Important distinction?
   **Answer (paste was cut off):** prediction estimates likely demand, while the inventory decision must also weigh costs
   and constraints (prescriptive optimization).
