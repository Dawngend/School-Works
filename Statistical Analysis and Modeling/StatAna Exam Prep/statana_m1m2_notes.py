"""Build the CS0073 Modules 1 and 2 written reviewer from the supplied slides."""

from pathlib import Path

from docx.shared import Inches

from notes_lib import Notes


OUTPUT = Path(__file__).resolve().parent.parent / "PAMESA - StatAna M1-M2 Reviewer.docx"


def build():
    n = Notes(
        "StatAna M1-M2 Reviewer",
        "CS0073 Statistical Analysis and Modeling. Modules 1 and 2 of the midterm. "
        "Memory Aid boxes are study cues, not slide text.",
    )
    n.doc.sections[0].top_margin = Inches(0.75)
    n.doc.sections[0].bottom_margin = Inches(0.75)

    n.h1("Part 1: Module 1, Foundations and Descriptive Analytics")
    n.h2("Data Value Chain")
    n.p("A value chain turns inputs into valuable outputs. The slide's analogy moves from coffee beans "
        "(raw material, storage), to instant coffee mix (processed material, inventory), to a coffee "
        "beverage (sales). Data creates value when insights lead to implemented decisions.")
    n.numbered([
        "**Transactional Data:** raw records of events, such as purchases, claims, transfers, or payments.",
        "**Database:** store, access, query, join tables, and aggregate data. This is sourcing data through analytic queries.",
        "**Analytics:** describe distributions and trends, examine correlations and relationships, and measure model strength.",
        "**Application:** test outcomes from varied inputs, scenarios, and sensitivity analysis; put analysis within reach of users.",
        "**Decision:** use the application to act on insights and shorten repetitive tasks. Implemented action realizes data value.",
    ])
    n.memory("**T-D-A-A-D:** Transactional data, Database, Analytics, Application, Decision. Raw coffee becomes a drink; raw data becomes an action.")

    n.h2("Five Data Sources")
    n.numbered([
        "**Transactional data:** structured details of a transaction, such as a purchase or payment.",
        "**Contractual, subscription, or account data:** product type together with customer characteristics.",
        "**Surveys:** questionnaires that collect sociodemographic and behavioral information from a group.",
        "**Data poolers:** companies that collect data for a purpose and sell it to enrich another source.",
        "**Unstructured data:** material outside a traditional row-column database, including media, audio, sensor data, text, email, web pages, and PDFs.",
    ])
    n.memory("**T-C-S-P-U:** Transactions, Contracts/accounts, Surveys, Poolers, Unstructured material.")

    n.h2("Gartner Analytic Ascendancy Model")
    n.p("The model moves toward greater value and difficulty. Descriptive gives hindsight and information; "
        "diagnostic gives insight; predictive gives foresight; prescriptive adds optimization.")
    n.table(["Type", "Question", "Role"], [
        ["Descriptive", "What happened?", "Hindsight; information"],
        ["Diagnostic", "Why did it happen?", "Insight"],
        ["Predictive", "What will happen?", "Foresight"],
        ["Prescriptive", "How can we make it happen?", "Optimization"],
    ], [1.4, 2.4, 2.7])
    n.memory("**What, Why, Will, How:** Descriptive, Diagnostic, Predictive, Prescriptive. Value and difficulty rise together.")

    n.h2("Descriptive Analytics")
    n.p("Descriptive analytics asks what happened or is happening. Its two primary techniques are "
        "**data aggregation** and **data presentation**.")
    n.table(["Branch", "Measures Or Output"], [
        ["Numerical summaries", "Totals and ratios"],
        ["Central tendency", "Mean, median, mode"],
        ["Variation", "Range, variance, standard deviation"],
        ["Shape", "Skewness, kurtosis"],
        ["Position", "Percentiles, quantiles, quartiles"],
        ["Tabulation and visualization", "Tables and charts"],
    ], [2.1, 4.4])
    n.memory("**C-V-S-P:** Center, Variation, Shape, Position. Center = mean/median/mode; variation = range/variance/standard deviation; shape = skewness/kurtosis; position = percentiles/quantiles/quartiles.")
    n.watch("The Excel section on slide p21 belongs to **Module 1 Subtopic 2, Descriptive Measures in Excel** (slide says \"Module 2 Submodule 2\").")

    n.h2("Excel Descriptive Functions")
    n.table(["Function", "What It Does"], [
        ["SUM(range)", "Adds numbers."],
        ["SUMIF(range, criteria, sum_range)", "Adds values meeting one criterion."],
        ["AVERAGE(range)", "Finds the arithmetic mean."],
        ["AVERAGEIF(range, criteria, average_range)", "Averages values meeting one criterion. (slide says AVERAGE(range,criteria,average_range))"],
        ["MEDIAN(range)", "Returns the middle value."],
        ["MIN(range) / MAX(range)", "Returns the smallest / largest value."],
        ["SMALL(range, k) / LARGE(range, k)", "Returns the kth smallest / largest value."],
        ["COUNT(range)", "Counts cells containing numbers."],
        ["COUNTA(range)", "Counts nonblank cells."],
        ["COUNTBLANK(range)", "Counts blank cells."],
        ["COUNTIF(range, criterion)", "Counts cells meeting one criterion."],
        ["COUNTIFS(...)", "Counts cells meeting multiple criteria."],
        ["SUMIFS(...)", "Sums values meeting multiple criteria."],
        ["AVERAGEIFS(...)", "Averages values meeting multiple criteria."],
        ["VAR(range) / VARP(range)", "Sample / population variance; square of standard deviation."],
        ["STDEV(range) / STDEVP(range)", "Sample / population standard deviation. (slide says STEVP)"],
        ["QUARTILE(range, quart)", "Returns a quartile, including Q1 and Q3."],
        ["PERCENTILE(range, k)", "Returns a value at a specified percentile."],
    ], [2.7, 3.8])
    n.memory("**Count, conditional, location, spread, position:** COUNT-family; IF/IFS; AVERAGE/MEDIAN/MIN/MAX; VAR/STDEV; QUARTILE/PERCENTILE/SMALL/LARGE.")
    n.watch("**COUNT** counts numbers; **COUNTA** counts nonblank cells; **COUNTBLANK** counts blank cells.")
    n.watch("**VAR and STDEV use a sample; VARP and STDEVP use a population.**")

    n.h2("Excel Slide Examples And Results")
    n.table(["Slide", "Example And Result"], [
        ["p25", "Enrollment: COUNT(student numbers) = 72; COUNTA(exam scores) = 69 took the exam; COUNTBLANK = 3 absent."],
        ["p26", "On-time performance: COUNT = 16; AVERAGE = 96.9%; VAR = 4.8; STDEV = 2.1."],
        ["p27", "Order status: Complete COUNTIF/COUNTIFS = 4, SUMIFS total = 366.50; Pending count = 2, shown total = 366.50; Complete OR Pending count = 6, shown total = 527.00. The displayed subtotals conflict with the displayed combined total."],
        ["p28", "AVERAGEIFS telephone expense: North = 275; South = 200."],
        ["p29", "Sales-rep MIN/MAX: January 2,300/3,800; February 2,200/3,600."],
        ["p30", "MEDIAN of EV/EBITDA multiples 2.5, 0.5, 1.4, 8.7, 2.7, 3.6 = 2.6."],
        ["p31", "QUARTILE real-estate prices: Q1 = 387,000; Q3 = 639,000; IQR = 252,000; bounds 9,000 and 1,017,000; 5,500,000 and 1,095,000 flagged."],
        ["p32", "Age percentiles (10th to 100th): 25, 30, 34, 39, 42, 48, 52, 56, 60, 65. At the 10th percentile, 10% are below age 25."],
        ["p33", "LARGE(Table[Speed], k): k = 1 gives 120; 2 gives 100; 5 gives 90; 10 gives 78."],
        ["p34", "SMALL(Table[Time], k): fastest 0:57:15; second 1:10:33; third 1:21:35."],
        ["p35", "Pivot table: rows Gender; columns Region; filter Paid With; values Sum of Total Cost."],
    ], [0.65, 5.85])
    n.memory("**Slide sequence:** attendance, on-time performance, order status, telephone expense, monthly sales, median multiples, quartile outliers, age percentiles, speed rank, time rank, pivot table.")
    n.watch("**Median resists extreme values better than mean.** The EV/EBITDA slide selects median for that reason.")

    n.h2("Quartiles, Percentiles, and Outliers")
    n.p("Q1 marks the value below which 25% of observations lie; Q3 marks 75%. For the slide's prices, "
        "**IQR = Q3 - Q1 = 639,000 - 387,000 = 252,000**. Multiply IQR by 1.5 to get 378,000. "
        "Lower bound = 387,000 - 378,000 = **9,000**. Upper bound = 639,000 + 378,000 = "
        "**1,017,000**. The prices **1,095,000** and **5,500,000** exceed the upper bound.")
    n.watch("**Outlier fences use 1.5 x IQR**, then subtract from Q1 or add to Q3.")
    n.p("A percentile is a position in an ordered distribution. The age slide divides people into ten equal groups: "
        "its 10th percentile is age 25, meaning 10% are below age 25.")

    n.h2("Descriptive Tools and Process Control")
    n.numbered([
        "**Pivot table:** organize and summarize data by row, column, filter, and value fields. The slide uses Gender, Region, Paid With, and Sum of Total Cost.",
        "**Moving average:** average observations over a chosen number of past periods to smooth noise and reveal trends; the slide compares actual and forecast lines.",
        "**Pareto chart:** bars from highest to lowest frequency or cost, with a cumulative percentage line, to prioritize which problem to address first.",
        "**Statistical process control:** monitor variation to find special causes and signal corrective action. All processes vary; the goal is to reduce variation.",
    ])
    n.memory("**P-M-P-S:** Pivot summarizes, Moving average smooths, Pareto prioritizes, SPC monitors.")
    n.p("A control chart has a **center line at the average** and **upper and lower control limits** based "
        "on variability, set at **3 sigma** by default. Points within limits show common cause variation "
        "natural to an in-control process; points outside show special cause variation, often from external "
        "sources, and an out-of-control process.")
    n.watch("**Common cause = in control; special cause = not in control.**")

    n.h1("Part 2: Module 2, Diagnostic Analytics")
    n.doc.paragraphs[-1].paragraph_format.page_break_before = True
    n.p("Diagnostic analytics asks **why it happened** using historical data. It investigates anomalies, "
        "relationships, and underlying drivers.")
    n.table(["Descriptive Analytics", "Diagnostic Analytics"], [
        ["Uses historical data", "Uses historical data"],
        ["Reconfigures data into an easily read format", "Identifies data anomalies"],
        ["Describes current performance or outcome", "Highlights trends and relationships"],
        ["Learns from the past", "Investigates underlying drivers"],
        ["Answers what", "Answers why"],
    ], [3.25, 3.25])
    n.h2("Three Functions")
    n.numbered([
        "**Identify anomalies:** notice unusual results.",
        "**Drill into analytics:** investigate details to discover an explanation.",
        "**Determine causal relationships:** examine possible causes. (slide says \"casual relationships\")",
    ])
    n.memory("**I-D-C:** Identify anomalies, Drill into analytics, determine Causal relationships.")
    n.h2("Question-To-Test Map")
    n.table(["Question", "Slide's Method"], [
        ["Which factors move together?", "Correlation coefficient"],
        ["Are categorical distributions different?", "Chi-Square"],
        ["Are two populations similar?", "ANOVA (F-test); analysis of means (Z-test, T-test)"],
    ], [3.25, 3.25])
    n.memory("**Move, Distribution, Population:** Correlation; Chi-Square; ANOVA/F-test or Z-test/T-test.")
    n.p("The objectives list Chi-Square, T-test, and one-way ANOVA, but these slides give no worked examples.")
    n.h2("Association and Correlation")
    n.p("**Association** is any general relationship between two variables, including a curved one. "
        "**Correlation** measures a linear relationship and may be positive, negative, or absent. "
        "A U-shaped pattern can be associated without a linear correlation.")
    n.watch("**Association is not always linear; correlation refers to a linear relationship.**")

    n.h1("One-Page Cram Sheet")
    n.doc.paragraphs[-1].paragraph_format.page_break_before = True
    n.table(["Topic", "Recall"], [
        ["Value chain", "Transactional data > Database > Analytics > Application > Decision; value arrives when action is implemented."],
        ["Five sources", "Transactions, contracts/accounts, surveys, data poolers, unstructured data."],
        ["Gartner", "Descriptive what/hindsight; diagnostic why/insight; predictive will/foresight; prescriptive how/optimization. Value and difficulty increase."],
        ["Descriptive", "Aggregate and present. Tree: central tendency, variation, shape, position; plus totals, ratios, tabulation, visualization."],
        ["Excel traps", "COUNT numbers, COUNTA nonblank, COUNTBLANK blank; VAR/STDEV sample, VARP/STDEVP population; AVERAGEIF spelling."],
        ["Middle and rank", "MEDIAN resists extremes; SMALL/LARGE return kth item; percentiles locate proportions."],
        ["IQR fences", "Q1 387,000; Q3 639,000; IQR 252,000; 1.5 x IQR 378,000; bounds 9,000 and 1,017,000."],
        ["Other tools", "Pivot summarizes; moving average smooths; Pareto prioritizes; control chart uses average center and 3-sigma limits."],
        ["Variation", "Common cause within limits = in control; special cause outside limits = not in control."],
        ["Diagnostic", "Why? Identify anomalies, drill into data, determine causal relationships."],
        ["Question > test", "Move together > correlation; distributions > Chi-Square; populations > ANOVA/F or Z/T."],
        ["Relationship", "Association can be curved; correlation is linear."],
    ], [1.35, 5.15])
    n.save(str(OUTPUT))


if __name__ == "__main__":
    build()
    print(OUTPUT)
