import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notes_lib import Notes

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def m3(n=None):
    solo = n is None
    if solo:
        n = Notes(
            "StatAna Module 3 Notes: Predictive Analytics and Regression Modeling",
            "CS0073, Module 3 Submodule 1. Built from the M3 slide text and the image-only regression output slides. "
            "The blue boxes are memory aids I made; they are not from the slides.",
        )

    n.h1("The Four Types Of Analytics")
    n.p("There are four types of analytics, each answering a different question. Each stage builds on the previous "
        "one, with increasing business value and complexity.")
    n.table(
        ["Type", "Question It Answers"],
        [
            ["**Descriptive**", "What has happened, or what is happening now?"],
            ["**Diagnostic**", "Why did it happen?"],
            ["**Predictive**", "What will likely happen?"],
            ["**Prescriptive**", "What should we do?"],
        ],
        [1.6, 4.9],
    )
    n.memory("**D-D-P-P in order of maturity: Descriptive, Diagnostic, Predictive, Prescriptive.** "
             "Each one answers a harder question than the last: What, Why, Will, Should.")

    n.h1("The Predictive Analytics Process")
    n.p("The process starts with three stages, then loops through a three-step cycle until the best model is "
        "selected:")
    n.numbered([
        "**Project Design:** kickoff meeting, understand the modeling objective, define acceptance criteria, "
        "document data and deployment requirements.",
        "**Data Sampling:** data extraction, apply filters and exclusions, identify external data sources.",
        "**Data Exploration:** exploratory data analysis (EDA), identify data dependencies and correlations, "
        "identify trends or anomalies in the data.",
        "**Data Modification:** data cleaning, data augmentation and transformation, feature selection.",
        "**Model Development:** apply different modeling techniques and select the final methodology.",
        "**Model Validation:** model performance review, feedback based on business knowledge and inputs from "
        "subject matter experts (SMEs).",
    ])
    n.p("Data Modification, Model Development, and Model Validation form a cycle that loops back into Project "
        "Design and best model selection, repeating until the final model is chosen.")
    n.memory("**P-S-E, then a cycle of M-D-V: Project design, Sampling, Exploration, then Modification, "
             "Development, Validation.** The last three steps are not one-and-done: they loop back into Project "
             "Design until the best model is selected.")

    n.h1("Defining A Linear Regression Problem")
    n.p("A linear regression problem is defined by two questions: **what is it?** (a relationship between two "
        "things) and **how is it used?** (one thing, A, causing an effect on another thing, B).")

    n.h2("The Simple Linear Regression Equation")
    n.p("The core formula is:")
    n.box("Formula", "y = βx + α + ε", "F2F2F2")
    n.table(
        ["Term", "Name", "Meaning"],
        [
            ["**y**", "Dependent variable", "The value to be predicted"],
            ["**x**", "Independent variable", "The value driving the prediction"],
            ["**β** (beta)", "Beta coefficient", "The rate multiplied to x"],
            ["**α** (alpha)", "Alpha intercept", "The baseline figure for y"],
            ["**ε** (epsilon)", "Error term", "The balancing figure"],
        ],
        [1.1, 1.8, 3.6],
    )
    n.memory("**Y depends, X drives, Beta is the Rate, Alpha is the Base, Epsilon Evens it out.**")

    n.h3("The Sales And Ad Spending Example")
    n.p("The slide maps the formula onto a real case: predicting sales from advertising spend.")
    n.table(
        ["Formula Term", "In This Example"],
        [
            ["y, dependent variable", "**Sales**"],
            ["x, independent variable", "**Ad Spending**"],
            ["β, beta coefficient", "**Sales Sensitivity**"],
            ["α, alpha intercept", "**Baseline Sales**"],
        ],
        [2.4, 4.1],
    )

    n.h3("Why The Error Term Exists")
    n.p("The slides give two reasons for including ε:")
    n.bullets([
        "To account for **unexplained variability** in the dependent variable from other relevant independent "
        "variables that may not have been included in the model.",
        "To capture **measurement error** in both the dependent and independent variables.",
    ])
    n.memory("**Error term = everything the model missed.** Missing variables, plus measurement mistakes.")

    n.h2("Multiple Linear Regression")
    n.p("You can have more than one predictor variable. The formula extends from one x to many:")
    n.box("Formula", "y = β1x1 + β2x2 + ... + βnxn + α + ε", "F2F2F2")
    n.p("This is the same equation as simple linear regression, just with more predictors (x1 through xn), each "
        "with its own beta coefficient.")

    n.h2("Splitting The Dataset")
    n.p("Before training a model, the original data is split so the model can be evaluated fairly:")
    n.numbered([
        "**Original Data** is split into **Training Data** and **Testing Data**.",
        "**Training Data** is split again into **Training** and **Validation**.",
    ])
    n.table(
        ["Split", "Purpose"],
        [
            ["**Training data**", "Trains the algorithm"],
            ["**Validation data**", "Used to tune and evaluate the model while it is being built"],
            ["**Testing data**", "The final performance evaluation of the finished model"],
        ],
        [1.8, 4.7],
    )
    n.memory("**Train to learn, Validate to tune, Test to grade.** The testing set is only touched at the very end.")

    n.pagebreak()
    n.h1("How To Read An Excel Regression Output")
    n.p("The slides show a regression of sales on three ad spend predictors (TV, radio, newspaper), with a sample "
        "size of **n = 140**. Read an Excel regression output in this order: Regression Statistics, ANOVA, then the "
        "coefficients (t-test) table.")

    n.h2("Step 1: Regression Statistics (R Square)")
    n.table(
        ["Statistic", "Value"],
        [
            ["Multiple R", "0.94536"],
            ["**R Square**", "**0.893710**"],
            ["Adjusted R Square", "0.891366"],
            ["Standard Error", "1.736514"],
            ["Observations", "140"],
        ],
        [2.4, 4.1],
    )
    n.p("**R Square (the coefficient of multiple determination, R2) is a goodness-of-fit measure.** It is normally "
        "expressed as a percentage and is interpreted as the amount of variability in the response explained by "
        "the independent variables. R2 is a figure of merit: the higher the R2, the better the model explains the "
        "variation in the response using the set of predictors. Here, **R Square 0.8937 means 89.37 percent of the "
        "variation in sales can be explained by TV, radio, and newspaper ad spend.**")
    n.watch("R2 almost always goes up when you add more predictors, even useless ones. **Adjusted R Square** "
            "corrects for the number of predictors, so it is the fairer number to compare between models with "
            "different numbers of predictors. On this slide Adjusted R Square (0.891366) is close to but slightly "
            "below R Square (0.893710), which is expected.")

    n.h2("Step 2: ANOVA Table")
    n.p("The ANOVA (Analysis of Variance) table is a decomposition of the total variation in the response into "
        "explained (pattern) and unexplained (error) parts. The explained variability is the amount of variation "
        "in the response variable that may be attributed to the predictors explicitly stated in the model. The "
        "unexplained variability is the amount of variation attributed to random error.")
    n.table(
        ["Source", "df", "SS", "MS", "F", "Significance F"],
        [
            ["Regression", "3", "3,448.264191", "1,149.421397", "381.1737161", "5.6038E-66"],
            ["Residual", "136", "410.1051657", "3.015479159", "", ""],
            ["Total", "139", "3,858.369357", "", "", ""],
        ],
        [1.3, 0.6, 1.5, 1.5, 1.3, 1.5],
    )
    n.p("**SS (Sum of Squares):** 3,448.26 is the variation in sales explained by the three predictors; 410.11 is "
        "the unexplained variation; the two sum to 3,858.37 (Total). A good fit shows the Regression SS much "
        "larger than the Residual SS, which is the case here.")
    n.p("**df (degrees of freedom), for n = 140 and 3 predictors:** Regression df = number of regression "
        "parameters minus one = **3**. Residual df = sample size minus number of regression parameters = **136**. "
        "Total df = Regression df + Residual df = **139**.")
    n.p("**MS (Mean Squares)** is each SS divided by its own df. MS has no physical meaning on its own; it exists "
        "to compute the F statistic.")
    n.p("**F and Significance F:** the F-test determines if the regression is meaningful for the data at hand. "
        "When the p-value (Significance F) is small, at least one predictor is significant. The rule of thumb is "
        "the p-value is low if it is less than the alpha significance level (usually 0.05). Here Significance F is "
        "5.6038E-66, an extremely small number, so the regression as a whole is significant.")
    n.memory("**\"When p is low, H0 must go!\"** A small p-value means you reject the null hypothesis (H0), which "
             "for the ANOVA F-test is \"none of the predictors matter.\"")
    n.watch("**df formula is a frequent trap.** Regression df = (number of parameters) minus 1 = 3. Residual df = "
            "n minus (number of parameters) = 140 - 4 = 136. Total df = 3 + 136 = 139. Do not confuse \"number of "
            "parameters\" (4: intercept plus 3 predictors) with \"number of predictors\" (3).")

    n.h2("Step 3: t-Tests Per Predictor")
    n.p("The t-test helps in assessing if an individual predictor is significant.")
    n.table(
        ["Predictor", "Coefficient", "SE", "t", "p-value"],
        [
            ["Intercept", "3.045142209", "0.391309656", "7.781924521", "1.60861E-12"],
            ["TV Ads (in 000s)", "0.047048681", "0.001701367", "27.6534582", "1.0917E-57"],
            ["Radio Ads (in 000s)", "0.179682989", "0.010782334", "16.6645727", "1.16107E-34"],
            ["Newspaper Ads (in 000s)", "-0.003005565", "0.007014537", "-0.42847661", "0.668982012"],
        ],
        [1.8, 1.3, 1.1, 1.1, 1.2],
    )
    n.bullets([
        "**TV ad spend:** p < 0.05, so TV ad spend is a **significant** predictor of sales.",
        "**Radio ad spend:** p < 0.05, so radio ad spend is a **significant** predictor of sales.",
        "**Newspaper ad spend:** p > 0.05 (0.668982012), so newspaper ad spend is an **insignificant** predictor "
        "of sales.",
    ])
    n.memory("**TV and Radio pass (low p, significant). Newspaper fails (high p, insignificant).** Newspaper is "
             "the one to remember as the \"odd one out\" on this slide.")
    n.watch("**Newspaper being insignificant is a favorite trap.** Its p-value (0.668982) is far above 0.05, and "
            "its coefficient is even negative. Do not assume all three predictors in a multiple regression are "
            "automatically useful just because the overall model (ANOVA) is significant.")

    n.h2("Step 4: Interpreting The Coefficients")
    n.p("Each coefficient is read **holding the other predictors constant**. The slide gives the fitted model as:")
    n.box("Fitted Model (as printed on the slide)", "Sales = 2.98 + 0.047 x TV + 0.178 x Radio", "F2F2F2")
    n.bullets([
        "**Intercept, 2.98:** the average sales if TV, radio, and newspaper ad spends are all 0.",
        "**0.047 (TV):** an estimated increase of 0.047 million (P47,000) in average sales for every P1,000 spent "
        "on TV ads, **holding radio and newspaper constant**.",
        "**0.178 (Radio):** an estimated increase of 0.178 million (P178,000) in average sales for every P1,000 "
        "spent on radio ads, **holding TV and newspaper constant**.",
    ])
    n.watch("**The slides disagree on the exact coefficients.** The p26 t-test table (the full model with all "
            "three predictors) gives Intercept 3.045142209, TV 0.047048681, Radio 0.179682989, Newspaper "
            "-0.003005565. The p28 fitted model slide instead prints **Sales = 2.98 + 0.047 x TV + 0.178 x Radio**, "
            "dropping newspaper entirely and rounding the other two numbers (2.98 vs 3.045, 0.178 vs 0.1797). "
            "The most likely explanation is the p28 model was refit without the insignificant newspaper predictor. "
            "If an exam question asks for \"the fitted model,\" quote the p28 numbers (2.98, 0.047, 0.178). If it "
            "asks for coefficients, SE, t, or p from the t-test table, use the p26 numbers.")

    n.h2("Step 5: Forecast Accuracy Measures")
    n.p("Once a model makes predictions, forecast error for each observation is e_i = Y - Y-hat (actual minus "
        "predicted). Four measures summarize how accurate the model is:")
    n.table(
        ["Measure", "Formula", "What It Means"],
        [
            ["**MAE** (Mean Absolute Error)", "(1/n) sum of |e_i|", "Average size of the errors, ignoring "
             "direction (over- or under-prediction)"],
            ["**MSE** (Mean Squared Error)", "(1/n) sum of e_i squared", "Average of the squared errors; squaring "
             "punishes big misses more than small ones"],
            ["**RMSE** (Root Mean Squared Error)", "square root of MSE", "MSE brought back to the original units "
             "of y, so it is easier to interpret than MSE"],
            ["**MAPE** (Mean Absolute Percentage Error)", "(1/n) sum of (|e_i| / Y), as a percentage", "Average "
             "error as a percentage of the actual value, so it is comparable across different scales"],
        ],
        [1.4, 1.9, 3.3],
    )
    n.memory("**MAE averages the absolute errors, in the original units. MSE averages the squared errors, in "
             "squared units, so it cannot be compared directly to MAE or RMSE. RMSE is the square root of MSE, "
             "back in the original units. MAPE expresses the average absolute error as a percentage of the "
             "actual value.**")
    n.watch("**MAPE divides by the actual Y, not the predicted value.** Mixing this up is a common exam trap.")

    n.h2("Practice: Read This Output")
    n.p("Using only the numbers already on these slides: a regression of sales on TV, radio, and newspaper ad "
        "spend, n = 140, gives R Square = 0.8937, ANOVA df = 3, 136, 139 with Significance F = 5.6038E-66, and "
        "t-test p-values of 1.09E-57 (TV), 1.16E-34 (Radio), and 0.6690 (Newspaper).")
    n.numbered([
        "**How much of the variation in sales does the model explain?** 89.37 percent (R Square 0.8937).",
        "**Is the overall regression significant?** Yes. Significance F (5.6038E-66) is far below 0.05.",
        "**Which predictors are individually significant at the 0.05 level?** TV and Radio (p < 0.05). Newspaper "
        "is not (p = 0.6690, above 0.05).",
        "**What are the Regression, Residual, and Total degrees of freedom?** 3, 136, and 139, matching "
        "3 predictors and n = 140.",
    ])

    if solo:
        n.save(os.path.join(OUT, "PAMESA - StatAna Summative 2 Reviewer.docx"))


def m4(n=None):
    solo = n is None
    if solo:
        n = Notes(
            "StatAna Module 4 Notes: Prescriptive Analytics and Decision Optimization",
            "CS0073, Module 4 Submodule 1. The blue boxes are memory aids I made; they are not from the slides.",
        )

    n.h1("Introduction To Prescriptive Analytics")
    n.p("**Prescriptive analytics is the most advanced form of business analytics.** It goes beyond describing "
        "what happened (descriptive), explaining why it happened (diagnostic), or predicting what will happen "
        "(predictive). Prescriptive analytics recommends actions to achieve desired outcomes and tells you the "
        "implications of each decision option. **It answers the question: \"What should we do?\"** By leveraging "
        "advanced algorithms, machine learning, and optimization techniques, prescriptive analytics enables "
        "data-driven decision making at scale.")
    n.memory("**Descriptive, Diagnostic, Predictive, Prescriptive = What, Why, Will, Should.** Prescriptive is the "
             "only one that tells you what action to take.")

    n.h1("The Evolution Of Analytics")
    n.table(
        ["Stage", "Question"],
        [
            ["**Descriptive Analytics**", "\"What happened?\" Examines historical data to understand past "
             "performance."],
            ["**Diagnostic Analytics**", "\"Why did it happen?\" Identifies causes and relationships in data."],
            ["**Predictive Analytics**", "\"What will happen?\" Forecasts future outcomes based on patterns."],
            ["**Prescriptive Analytics**", "\"What should we do?\" Recommends actions to optimize outcomes."],
        ],
        [1.9, 4.6],
    )
    n.p("Each stage builds upon the previous, with increasing business value and complexity. Prescriptive "
        "analytics represents the pinnacle of data-driven decision making.")

    n.h1("How Prescriptive Analytics Works: The Five-Step Process")
    n.numbered([
        "**Data Collection and Integration:** gather relevant historical and real-time data from multiple "
        "sources.",
        "**Predictive Modeling:** create models to forecast potential future outcomes.",
        "**Scenario Analysis:** evaluate multiple possible scenarios and their implications.",
        "**Optimization:** apply algorithms to determine the best course of action.",
        "**Action Recommendation:** deliver actionable insights to decision-makers.",
    ])
    n.p("This is an iterative process that continuously improves as more data becomes available and outcomes are "
        "measured.")
    n.memory("**D-P-S-O-A: Data, Predict, Scenario, Optimize, Act.** \"**D**ogs **P**lay **S**oftly **O**n "
             "**A**sphalt.\" Notice the predictive model (step 2) happens before the optimization (step 4).")

    n.h1("Key Technologies And Techniques")
    n.p("Prescriptive analytics leverages several advanced technologies to transform data into actionable "
        "recommendations:")
    n.table(
        ["Technology", "What It Does"],
        [
            ["**Machine Learning and AI**", "Algorithms that learn from data patterns to make predictions and "
             "improve over time without explicit programming."],
            ["**Optimization Algorithms**", "Mathematical techniques that find the best solution among "
             "alternatives, considering constraints and objectives."],
            ["**Simulation Modeling**", "Creating virtual scenarios to test different strategies and understand "
             "potential outcomes."],
            ["**Natural Language Processing**", "Enabling systems to understand and communicate recommendations "
             "in human language."],
            ["**Real-time Analytics**", "Processing data as it is created to provide immediate insights and "
             "recommendations."],
        ],
        [2.0, 4.5],
    )
    n.memory("**M-O-S-N-R: Machine learning, Optimization, Simulation, NLP, Real-time.** \"**M**y **O**wl **S**ings "
             "**N**ice **R**hymes.\"")

    n.h1("Business Applications By Industry")
    n.table(
        ["Industry", "Applications"],
        [
            ["**Healthcare**", "Patient treatment optimization, resource allocation, staff scheduling, and "
             "personalized medicine."],
            ["**Supply Chain**", "Inventory optimization, logistics routing, demand forecasting, and supplier "
             "selection."],
            ["**Financial Services**", "Portfolio optimization, risk management, fraud detection, and "
             "algorithmic trading."],
            ["**Manufacturing**", "Production scheduling, quality control, predictive maintenance, and resource "
             "allocation."],
            ["**Energy and Utilities**", "Grid optimization, energy trading, demand response, and renewable "
             "integration."],
        ],
        [1.8, 4.7],
    )
    n.memory("**H-S-F-M-E: Healthcare, Supply chain, Financial, Manufacturing, Energy.** Each industry gets its "
             "own flavor of \"optimize something.\"")

    n.h1("Enhancing Decision Making")
    n.p("Prescriptive analytics transforms organizational decision making from intuition-based to data-driven.")
    n.table(
        ["Benefit", "Explanation"],
        [
            ["**Reduced Decision Complexity**", "Simplifies complex decisions by evaluating numerous variables "
             "and constraints simultaneously."],
            ["**Increased Decision Speed**", "Enables faster decision-making through automated analysis and "
             "recommendation generation."],
            ["**Improved Decision Quality**", "Enhances outcomes by considering more factors and scenarios than "
             "humanly possible."],
            ["**Competitive Advantage**", "Organizations using prescriptive analytics gain an edge through "
             "optimized resource allocation and strategic planning."],
        ],
        [2.1, 4.4],
    )
    n.p("The result: better decisions, faster, across all levels of the organization.")
    n.memory("**R-I-I-C: Reduced complexity, Increased speed, Improved quality, Competitive advantage.** All four "
             "benefits start with a word meaning \"better than before.\"")

    n.h1("Implementation Challenges And Best Practices")
    n.p("Successfully implementing prescriptive analytics requires addressing several key challenges, each paired "
        "with its solution on the slide:")
    n.table(
        ["Challenge", "Solution"],
        [
            ["**Data Integration:** combining data from disparate sources with varying formats and quality.",
             "Implement robust data governance and ETL processes."],
            ["**Skill Gaps:** finding talent with expertise in both analytics and domain knowledge.",
             "Invest in training programs and cross-functional teams."],
            ["**Organizational Change:** shifting from intuition-based to data-driven decision making culture.",
             "Start with high-impact use cases and demonstrate ROI."],
            ["**Technology Selection:** choosing the right tools and platforms for specific business needs.",
             "Begin with pilot projects to evaluate technology fit."],
        ],
        [3.1, 3.4],
    )
    n.memory("**Pair each challenge with its fix: Data -> Governance/ETL, Skills -> Training, Change -> High-"
             "impact pilots and ROI, Tech choice -> Pilot projects.** The solution to \"people don't trust the "
             "data-driven culture\" is always to prove it works on a small scale first.")
    n.watch("Four challenges, four solutions, always in the same order on the slide: **Data Integration, Skill "
            "Gaps, Organizational Change, Technology Selection.** Do not swap \"training programs\" (the fix for "
            "skill gaps) with \"pilot projects\" (the fix for technology selection); both sound like \"start "
            "small\" but answer different problems.")

    n.h1("Future Trends")
    n.table(
        ["Trend", "What It Means"],
        [
            ["**Autonomous Decision Systems**", "Systems that not only recommend actions but can implement them "
             "with minimal human intervention."],
            ["**Augmented Analytics**", "AI-powered tools that make advanced analytics accessible to "
             "non-technical business users."],
            ["**Edge Computing**", "Prescriptive capabilities deployed at the edge for real-time decision making "
             "without latency."],
            ["**Explainable AI**", "Transparent algorithms that can explain the reasoning behind their "
             "recommendations."],
        ],
        [2.1, 4.4],
    )
    n.p("Prescriptive analytics represents the future of data-driven decision making. Organizations that "
        "successfully implement these capabilities will gain significant competitive advantages through "
        "optimized operations, enhanced customer experiences, and improved business outcomes.")
    n.memory("**A-A-E-E: Autonomous, Augmented, Edge, Explainable.** Autonomous acts for you; Augmented helps "
             "non-technical users; Edge removes latency; Explainable shows its reasoning.")

    if solo:
        n.save(os.path.join(OUT, "PAMESA - StatAna Summative 2 Reviewer.docx"))


def combined():
    n = Notes(
        "StatAna Summative 2 Reviewer: Modules 3 and 4",
        "CS0073 Statistical Analysis and Modeling. Covers Module 3 (Predictive Analytics and Regression Modeling) "
        "and Module 4 (Prescriptive Analytics and Decision Optimization). This also serves as the M3/M4 half of "
        "the midterm reviewer (midterm covers M1 to M4; M1 and M2 are not included here because those slides are "
        "not available yet). The blue boxes are memory aids I made; they are not from the slides.",
    )
    n.pagebreak()
    n.h1("What Is Inside")
    n.bullets([
        "**Part 1, Module 3:** the four types of analytics, the predictive analytics process, the linear "
        "regression equation and the Sales and Ad Spending example, multiple regression, the training/validation/"
        "testing split, a full walkthrough of how to read an Excel regression output using the slide's own "
        "numbers, and the four forecast accuracy measures.",
        "**Part 2, Module 4:** prescriptive analytics and \"what should we do?\", the evolution of analytics, "
        "the five-step prescriptive process, key technologies, business applications by industry, decision-"
        "making benefits, implementation challenges and solutions, and future trends.",
        "A single one-page cram sheet covering both parts comes at the very end. Read it last, right before "
        "the exam.",
    ])
    n.h2("Fast Memory Map")
    n.table(
        ["Topic", "Hook"],
        [
            ["Four analytics types", "Descriptive, Diagnostic, Predictive, Prescriptive = What, Why, Will, Should"],
            ["Predictive process", "Project design, Sampling, Exploration, then a cycle of Modification, "
             "Development, Validation"],
            ["Regression equation", "y = beta x + alpha + epsilon; Y depends, X drives, Beta is the Rate, Alpha "
             "is the Base, Epsilon Evens it out"],
            ["R Square", "0.8937 means 89.37 percent of sales variation explained"],
            ["ANOVA df (n=140, 3 predictors)", "3, 136, 139"],
            ["Significant predictors", "TV and Radio significant (p < 0.05); Newspaper is not (p = 0.6690)"],
            ["When p is low", "H0 must go"],
            ["Forecast error measures", "MAE plain, MSE squared, RMSE un-squared, MAPE percent of actual Y"],
            ["Prescriptive process", "Data, Predict, Scenario, Optimize, Act (5 steps)"],
            ["Prescriptive question", "\"What should we do?\""],
        ],
        [2.1, 4.4],
    )
    n.pagebreak()
    n.h1("Part 1: Module 3, Predictive Analytics and Regression Modeling")
    m3(n)
    n.pagebreak()
    n.h1("Part 2: Module 4, Prescriptive Analytics and Decision Optimization")
    m4(n)

    n.pagebreak()
    n.h1("One-Page Cram Sheet")
    n.table(
        ["Topic", "Remember"],
        [
            ["Four analytics types", "Descriptive (what happened), Diagnostic (why), Predictive (will happen), "
             "Prescriptive (should do)"],
            ["Predictive process", "Project Design, Data Sampling, Data Exploration, then a cycle of Data "
             "Modification, Model Development, Model Validation"],
            ["Regression equation", "y = beta x + alpha + epsilon"],
            ["Sales example", "y = Sales, x = Ad Spending, beta = Sales Sensitivity, alpha = Baseline Sales"],
            ["Multiple regression", "y = b1x1 + b2x2 + ... + bnxn + alpha + epsilon"],
            ["Dataset split", "Original -> Training + Testing; Training -> Training + Validation"],
            ["R Square", "Goodness-of-fit, percent of variation explained; here 0.8937 = 89.37 percent"],
            ["Adjusted R Square", "Corrects R Square for number of predictors; use it to compare models"],
            ["ANOVA SS", "Regression SS (explained) + Residual SS (unexplained) = Total SS"],
            ["ANOVA df, n=140, 3 predictors", "Regression 3, Residual 136, Total 139"],
            ["ANOVA MS", "SS divided by its df; used only to compute F"],
            ["Significance F", "p-value of the whole regression; small means at least one predictor matters"],
            ["When p is low", "H0 must go (reject the null hypothesis)"],
            ["t-test per predictor", "p < 0.05 significant; here TV and Radio significant, Newspaper is not"],
            ["Coefficient reading", "Holding the other predictors constant"],
            ["p26 vs p28 model", "p26 t-test table keeps all 3 predictors; p28 fitted model drops newspaper and "
             "rounds (2.98, 0.047, 0.178)"],
            ["MAE / MSE / RMSE / MAPE", "Average absolute error / average squared error (squared units) / root "
             "of MSE (original units) / absolute error as a percent of actual Y"],
            ["Prescriptive analytics", "\"What should we do?\"; most advanced, most complex analytics stage"],
            ["Five-step process", "Data Collection, Predictive Modeling, Scenario Analysis, Optimization, Action "
             "Recommendation"],
            ["Key technologies", "Machine Learning/AI, Optimization Algorithms, Simulation, NLP, Real-time "
             "Analytics"],
            ["Challenge -> Solution", "Data Integration -> governance/ETL; Skill Gaps -> training; "
             "Organizational Change -> high-impact pilots/ROI; Technology Selection -> pilot projects"],
            ["Future trends", "Autonomous Decision Systems, Augmented Analytics, Edge Computing, Explainable AI"],
        ],
        [2.1, 4.4],
    )
    n.save(os.path.join(OUT, "PAMESA - StatAna Summative 2 Reviewer.docx"))


if __name__ == "__main__":
    combined()
    print("done")
