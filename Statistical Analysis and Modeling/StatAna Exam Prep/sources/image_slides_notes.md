# StatAna (CS0073) M3 and M4 image-only slide content, transcribed by Claude from the slide pictures

M3 Predictive Analytics & Regression Modeling (Module 3 Submodule 1)
- p4 three analytics: Descriptive = What has happened or what is happening now?; Diagnostic = Why it happened?;
  Predictive = What will likely happen?
- p5 Predictive Analytics Process: Project Design (kickoff meeting, understand modeling objective, define acceptance
  criteria, document data and deployment requirement) -> Data sampling (data extraction, apply filters and exclusions,
  identify external data sources) -> Data Exploration (EDA, identify data dependencies and correlations, identify trends
  or anomalies) -> cycle of Data modification (data cleaning, data augmentation and transformation, feature selection),
  Model Development (apply different modeling techniques and select final methodology), Model Validation (model
  performance review, feedback based on business knowledge and inputs from SMEs) -> Project Design / Best model selection.
- p6 Defining a Linear Regression Problem: "What is it?" (circle + circle = circle) and "How is it used?" (A CAUSE -> B EFFECT).
- p7 scatter: Y = dependent variable (vertical), X = independent variable (horizontal), regression line through
  observations; y = beta x + alpha + epsilon.
- p8 y = beta x + alpha + epsilon: y dependent (value to be predicted); x independent (value driving prediction);
  beta = beta coefficient (rate multiplied to X); alpha = alpha intercept (baseline figure for y);
  epsilon = error term (balancing figure).
- p10 example: y = Sales, x = Ad Spending, beta = Sales Sensitivity, alpha = Baseline Sales.
- p11 demo "Sales Attribution": you are the Advertising Manager asked for the effect of TV ad spend on sales:
  1. create a scatter plot, 2. display the regression equation.
- p12 Excel: TV Ads (in 000s) vs Sales (in m); chart "Effect of TV Ads Spend on Sales" trendline
  y = 0.0475x + 7.0326, R^2 = 0.6119. Steps: scatter plot; Excel formulas for intercept and slope, R2 and standard error.
- p13 multiple: y = b1x1 + b2x2 + ... + bnxn + alpha + epsilon; more than one predictor (x1 to xn).
- p14 example of a scatterplot matrix (iris: sepal length/width, petal length/width).
- p15 demo "Marketing Mix Modeling": effect on revenue of TV, radio and newspaper ad spend.
- p16 Splitting the dataset: Original Data -> Training Data + Testing Data; Training split again into Training and
  Validation. Training data trains the algorithm; validation data is used to tune/evaluate; testing data is the
  final performance evaluation of the final model.
- p17 Excel SUMMARY OUTPUT (training set): Multiple R 0.9558, R Square 0.9135, Adjusted R Square 0.9095,
  Standard Error 1.5921, Observations 69; ANOVA Regression df 3 SS 1740.53 MS 580.18 F 228.88 Sig F 1.75E-34;
  Residual df 65 SS 164.77 MS 2.53; Total df 68 SS 1905.30; Intercept 3.356 (SE 0.531, t 6.32, p 2.72E-08).
- p20 Regression Statistics (full data): Multiple R 0.94536, R Square 0.893710, Adjusted R Square 0.891366,
  Standard Error 1.736514, Observations 140. "R2 = 0.8937 means 89.37% of the variation in sales can be explained by
  TV, radio, and newspaper ad spend."
- p22-p25 ANOVA table: Regression df 3, SS 3448.264191, MS 1149.421397, F 381.1737161, Significance F 5.6038E-66;
  Residual df 136, SS 410.1051657, MS 3.015479159; Total df 139, SS 3858.369357.
  SS = Sum of Squares: 3,448.26 = variation in sales explained by the three predictors; 410.11 = unexplained;
  they sum to 3,858.37. Good fit if Regression SS is much larger than Residual SS.
  df = degrees of freedom: Regression df = number of regression parameters minus one; Residual df = sample size
  minus number of regression parameters; Total df = sum of the two.
  MS = Mean Squares = each SS divided by its df; no physical meaning but used to compute the F statistic.
  F-test determines if the regression is meaningful for the data at hand. When the p-value (Significance F) is
  small, at least one predictor is significant. "When p is low, H0 must go!" Rule of thumb: p-value is low if it is
  less than the alpha significance level.
- p26 t-tests table: Intercept coef 3.045142209, SE 0.391309656, t 7.781924521, p 1.60861E-12;
  TV Ads (in 000s) 0.047048681, SE 0.001701367, t 27.6534582, p 1.0917E-57;
  Radio Ads (in 000s) 0.179682989, SE 0.010782334, t 16.6645727, p 1.16107E-34;
  Newspaper Ads (in 000s) -0.003005565, SE 0.007014537, t -0.42847661, p 0.668982012.
  TV and Radio p < 0.05 significant; Newspaper p > 0.05 insignificant.
- p28 fitted model as printed on the slide: Sales = 2.98 + 0.047 x TV + 0.178 x Radio. Intercept 2.98 = average sales
  if TV, radio and newspaper spends are all 0; 0.047 = estimated increase of 0.047 million (P47K) in average sales for
  every P1,000 TV spend, holding radio and newspaper constant; 0.178 = P178K per P1,000 radio spend, holding TV and
  newspaper constant. NOTE: these numbers differ from the p26 table (3.045, 0.047, 0.180); the slide likely refit
  without newspaper. Use the slide's numbers when quoting p28.
- p29 forecast accuracy measures, e_i = Y - Y-hat: MAE = (1/n) sum |e_i|; MSE = (1/n) sum e_i^2;
  MAPE = (1/n) sum |e_i| / Y (as a percentage); RMSE = sqrt((1/n) sum e_i^2).
- p30 project: groups of max 5; dataset from Data.gov.ph; derive an objective; apply the techniques; Python or Excel.

M4 Prescriptive Analytics & Decision Optimization: all text is in the extracted .txt (no image-only content).
