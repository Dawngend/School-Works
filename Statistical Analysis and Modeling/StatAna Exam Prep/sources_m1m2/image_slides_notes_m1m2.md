# StatAna (CS0073) M1 and M2 picture-slide content, transcribed by Claude from the slides

M1 Foundations of Data Analytics & Exploratory Data Analysis (file covers Module 1 Submodule 1 AND a section the
slide labels "Module 2 Submodule 2" (p21), which is the Excel descriptive-measures part of Module 1. Treat p21-p40 as
Module 1 Subtopic 2 "Descriptive Measures in Excel"; the "Module 2" label on p21 is a slide typo.)
- p5 value chain analogy: coffee beans (raw material, storage) -> instant coffee mix (processed material,
  inventory) -> coffee beverage (sales).
- p6 Data value chain: Transactional Data -> Database -> Analytics -> Application -> Decision.
- p7 five data sources: Transactional data; Contractual, subscription or account data; Surveys; Data poolers;
  Unstructured data.
- p13 Gartner Analytic Ascendancy model (x = Difficulty, y = Value): Descriptive "What happened?" (hindsight,
  information) -> Diagnostic "Why did it happen?" (insight) -> Predictive "What will happen?" (foresight) ->
  Prescriptive "How can we make it happen?" (optimization). NOTE M4 phrases prescriptive as "What should we do?";
  both are the same idea.
- p14 mapping onto the chain: Database stage = SOURCING DATA (analytic queries); Analytics stage = ANALYZING DATA
  (descriptive, diagnostic, predictive); Application stage = ANALYZING DATA (prescriptive).
- p15 tasks per stage: Database = accessing and querying databases, join tables, aggregating data; Analytics =
  distribution, trending, correlation, model relationship, measure model strength; Application = test outcomes from
  various input, scenarios, sensitivity analysis; Decision = shorten repetitive task, allow users to interact with data.
- p17 two primary techniques of descriptive analytics: Data Aggregation and Data Presentation.
- p18 Descriptive analysis tree: Numerical Summaries (Total; Ratios; Central Tendency = mean, median, mode;
  Variation = range, variance, standard deviation; Shape = skewness, kurtosis; Position = percentiles, quantiles,
  quartiles) and Tabulation and Visualization.
- p23-p24 Excel function table (verbatim meanings): SUM, SUMIF(range, criteria, sum_range), AVERAGE, AVERAGEIF
  (slide misprints it as AVERAGE(range,criteria,average_range); the correct function is AVERAGEIF), MEDIAN, MAX, MIN,
  SMALL(range,k)/LARGE(range,k) = kth smallest/largest, COUNT = cells with numbers, COUNTA = non-blank cells,
  COUNTBLANK = blank cells, COUNTIF(range,value), VAR (sample) / VARP (population) = square of std dev,
  STDEV (sample) / STDEVP (population; slide misprints "STEVP").
- p25 example: 72 enrolled = COUNT(student numbers); 69 took the exam = COUNTA(exam scores); 3 absent = COUNTBLANK.
- p26 on-time performance (%) example: sample size 16 (COUNT), mean 96.9 (AVERAGE), variance 4.8 (VAR), std dev 2.1
  (STDEV).
- p27 COUNTIF/COUNTIFS/SUMIFS by order Status: Complete count 4 total 366.50; Pending count 2 total 366.50 (as shown);
  Complete OR Pending count 6 total 527.00 using SUM(COUNTIFS(...,{"Pending","Complete"})) and
  SUM(SUMIFS(...,{"Complete","Pending"})).
- p28 AVERAGEIFS average telephone expense: North 275, South 200.
- p29 MIN/MAX per month across sales reps: Jan min 2,300 max 3,800; Feb min 2,200 max 3,600.
- p30 MEDIAN of EV/EBITDA multiples (2.5, 0.5, 1.4, 8.7, 2.7, 3.6) = 2.6; median chosen because data has extreme values.
- p31 QUARTILE outlier test on real-estate prices: Q1 387,000; Q3 639,000; IQR = Q3 - Q1 = 252,000; lower bound =
  Q1 - 1.5 x IQR = 9,000; upper bound = Q3 + 1.5 x IQR = 1,017,000; prices above (5,500,000 and 1,095,000) are flagged
  outliers ("Y"). Q1 = value under which 25% of data lie; Q3 = 75%.
- p32 PERCENTILE: divide people into 10 equal groups by age; 10th to 100th percentiles (ages 25, 30, 34, 39, 42, 48,
  52, 56, 60, 65); interpretation "10% of the individuals are aged below 25", etc.
- p33 LARGE(Table[Speed], k): k=1 -> 120, k=2 -> 100, k=5 -> 90, k=10 -> 78.
- p34 SMALL(Table[Time], k): winning time 0:57:15, 2nd 1:10:33, 3rd 1:21:35.
- p35 PIVOT TABLE: rows Gender, columns Region, filter Paid With, values Sum of Total Cost.
- p36 Moving average chart (actual vs forecast).
- p37 Pareto chart: bars sorted longest left to shortest right plus cumulative % line; prioritization tool.
- p40 Control chart: a center line (the average, also called the control line) and upper/lower control limits;
  limits are based on the variability in the data and set at 3-sigma by default; points inside = common cause
  variation; points outside the limits = special cause variation.
- p38 typo: "signing the need" means "signaling the need".

M2 Diagnostic Analytics & Statistical Inference (10 slides only)
- p4 Descriptive vs Diagnostic table: both use historical data; descriptive reconfigures data into easily read
  format, describes current performance/outcome, learns from the past, answers "what"; diagnostic identifies data
  anomalies, highlights data trends and relationships, investigates underlying drivers, answers "why".
- p5 three functions: Identify Anomalies; Drill into analytics (discovery); Determine causal relationships (slide
  misspells "casual"; the correct word is causal).
- p6 question -> test: Which factors move together? -> Correlation coefficient. Are there differences in
  distribution? -> Categorical distributions (Chi-Square). Are two populations similar? -> ANOVA (F-test) and
  analysis of means (Z-test, T-test).
- p7 Association = general relationship between two random variables (a U-shaped curve is associated but not
  linear); Correlation = a measure of association that refers to a LINEAR relationship; scatter plots of positive,
  negative and no correlation.
- The M2 objectives mention performing Chi-Square, T-test and one-way ANOVA, but these slides contain no worked
  examples of them; only the question-to-test mapping above.
