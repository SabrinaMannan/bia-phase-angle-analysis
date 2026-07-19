# BIA Phase Angle Statistical Analysis

**Author:** Sabrina Mannan

## Overview

This repository reproduces the statistical analysis of baseline body composition and Bioelectrical Impedance Analysis (BIA) phase angle using Python. The workflow was adapted from an existing R analysis to create a fully reproducible Python pipeline.

The analysis compares body composition measurements among four study groups:

- EGD Healthy
- EGD Low BMI
- Pregnant Healthy
- Pregnant Low BMI

The notebook includes data preprocessing, descriptive statistics, hypothesis testing, regression analysis, diagnostic assessment, and publication-quality visualizations.


## Objectives

The primary objective was to describe and compare baseline body composition measured by BIA among four study groups and evaluate factors associated with phase angle.


## Dataset

The original dataset is confidential and **is not included** in this repository.

The dataset contains baseline measurements including:

- Phase angle
- Height
- Weight
- BMI
- Age
- Education
- Household characteristics
- Socioeconomic indicators
- Pregnancy status


## Analysis Workflow

The notebook follows this workflow:

1. Import libraries
2. Load dataset
3. Data preprocessing
4. Exploratory data analysis
5. Normality assessment
6. Baseline descriptive statistics
7. Phase angle summary analysis
8. One-way ANOVA
9. Tukey HSD post-hoc analysis
10. Kruskal–Wallis test
11. Spearman correlation
12. Univariate linear regression
13. Multiple linear regression
14. Regression diagnostics
15. Data visualization
16. Save outputs

---

## Statistical Methods

The following statistical methods were implemented:

- Shapiro–Wilk normality test
- Q-Q plots
- Descriptive statistics
- One-way ANOVA
- Tukey HSD post-hoc test
- Kruskal–Wallis test
- Spearman correlation
- Univariate linear regression
- Multiple linear regression
- Variance Inflation Factor (VIF)
- Residual diagnostics



## Visualizations

The notebook generates:

- Boxplots
- Violin plots
- Q-Q plots
- Residual vs Fitted plots
- Publication-ready figures with statistical annotations


These include:

- Baseline characteristic tables
- Phase angle summary tables
- ANOVA results
- Tukey HSD comparisons
- Correlation results
- Regression results
- Regression diagnostics
- Publication-quality figures






## Confidentiality

The dataset used in this project contains confidential research data and is not publicly available. Therefore, only the analysis code and generated outputs are shared.



## Skills Demonstrated

- Python for statistical analysis
- Data preprocessing
- Stata data handling (`.dta`)
- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Linear regression
- Regression diagnostics
- Scientific visualization
- Reproducible research workflows



## Acknowledgements

This notebook reproduces and translates an existing R-based statistical workflow into Python for reproducible research and educational purposes.
