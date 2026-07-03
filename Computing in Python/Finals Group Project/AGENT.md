# Project Story

The entire notebook follows one historical narrative.

Title:

Pandemic Flight:
How Work-From-Home Changed Philippine Real Estate

The story should naturally flow through four chapters:

1. The Messy Reality
2. The Location Map
3. The Price of Space
4. The WFH Shift

Do NOT introduce unrelated analyses.

Do NOT change the story.

Do NOT invent conclusions that cannot be supported by the dataset.

---

# Required Workflow

Always follow this order.

## Phase 1

Import libraries.

Load dataset.

Inspect dataset.

Display:

- head()
- info()
- describe()
- missing values

---

## Phase 2

Pre-processing

Expected cleaning tasks include:

- Handle "na" values
- Remove invalid rows only when justified
- Clean the Price column
- Convert Price into numeric
- Convert Bedrooms into numeric
- Convert Bathrooms into numeric
- Create a clean Region column from Location
- Strip unnecessary commas and symbols
- Ensure proper datatypes

Never fabricate data.

Never impute values without explanation.

---

## Phase 3

Exploratory Data Analysis

Required analyses include:

### Discovery 1

Location Distribution

Visualization:
Bar Chart or Count Plot

Purpose:
Show where most property listings are concentrated.

---

### Discovery 2

Bedrooms vs Price

Visualization:
Scatter Plot

Purpose:
Illustrate the relationship between space and housing prices.

Different regions may be color-coded if appropriate.

---

### Discovery 3

Urban vs Provincial Prices

Visualization:
Box Plot

Purpose:
Compare price distributions between Metro Manila and Provincial areas.

---

## Phase 4

Insights

Every visualization must be followed by:

- observations
- interpretation
- business insight

Never leave a graph unexplained.

---

# Coding Standards

Write beginner-friendly Python.

Prefer readability over cleverness.

Every code block should contain comments explaining:

- what it does
- why it is needed

Avoid one-line unreadable code.

Variable names should be descriptive.

---

# Visualization Standards

Use:
matplotlib
seaborn

Every figure must include:

- title
- axis labels
- readable font sizes

Rotate labels when necessary.

Use consistent color palettes.

Avoid clutter.

---

# Documentation Style

Use Markdown heavily.

Each notebook section should contain:

## Heading

### Objective

### Code

### Output

### Explanation

The notebook should read like a report rather than a script.

---

# Narrative Rules

The notebook is telling a story.

Maintain the following sequence:

Messy Data

↓

Cleaning

↓

Location Analysis

↓

Price Analysis

↓

Business Insight

↓

Conclusion

Do not jump randomly between topics.

---

# Allowed Conclusions

Conclusions must only come from observed data.

Use cautious wording such as:

"The dataset suggests..."
"The analysis indicates..."
"There appears to be..."

Avoid absolute statements.

Never claim causation when only correlation is shown.

---

# Forbidden Behavior

Never:

- invent statistics
- invent percentages
- fabricate trends
- hallucinate missing columns
- assume data that does not exist
- reference years if the dataset has no dates
- create machine learning models
- perform forecasting
- add neural networks
- use TensorFlow
- use PyTorch
- recommend SQL
- recommend Power BI
- recommend Tableau
- recommend Streamlit
- convert this into a web application

Stay within the project scope.

---

# Expected Dataset Columns

Only use columns that actually exist.

Before referencing any column, verify it exists.

Do not hallucinate additional features.

---

# Assistant Behavior

Always inspect the notebook before suggesting code.

If uncertain about a column name:

STOP.

Ask for clarification instead of guessing.

Never generate code against imaginary columns.

---

# Output Expectations

Generated code should be:

- executable
- commented
- beginner-friendly
- properly formatted
- compatible with Jupyter Notebook

---

# Presentation Goal

The notebook should naturally support a 5–10 minute presentation.

Each section should be explainable verbally.

Every graph should answer one business question.

---

# Final Deliverables

The finished notebook should contain:

✔ Introduction

✔ Dataset Overview

✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Three Required Visualizations

✔ Business Insights

✔ Conclusion

The notebook should export cleanly to PDF without requiring additional modifications.

---

# Communication Style

When assisting:

- Think like a Python instructor.
- Explain decisions briefly.
- Avoid unnecessary complexity.
- Prioritize correctness over sophistication.
- If multiple approaches exist, recommend the simplest reliable solution.

The goal is a polished, academically appropriate final project—not an advanced data science showcase.

---

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# First, let's read the AGENT.md file to understand the dataset structure
with open("Finals Group Project in Computing in Python/AGENT.md", "r") as file:
    agent_content = file.read()
print("AGENT.md content preview:")
print(agent_content[:500])  # Display first 500 characters to understand the dataset

# Now proceed with loading the actual dataset
# Assuming the dataset is in CSV format and located in the same directory
# We'll need to verify the exact filename from the directory listing
try:
    # Try to list files in the directory to find the dataset
    import os
    dataset_files = [f for f in os.listdir("Finals Group Project in Computing in Python") if f.endswith('.csv')]
    print("\nAvailable dataset files:")
    print(dataset_files)

    # Load the first CSV file found (assuming there's only one dataset)
    if dataset_files:
        dataset_path = os.path.join("Finals Group Project in Computing in Python", dataset_files[0])
        real_estate_data = pd.read_csv(dataset_path)
        print("\nDataset loaded successfully!")
    else:
        print("\nNo CSV files found in the directory. Please verify the dataset location.")
except Exception as e:
    print(f"\nError loading dataset: {e}")
    print("Please verify the dataset path and format.")

# Check directory contents to locate dataset
!ls -R "Finals Group Project in Computing in Python"

