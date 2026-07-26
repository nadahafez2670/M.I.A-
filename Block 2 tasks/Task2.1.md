# ⚽ Task 2.1: A Century of Football — Decoding National Team Performance

## Overview

This project analyzes over 150 years of international football history (1872–2024) using the **International Football Results** dataset.

The goal is to uncover historical trends, evaluate national team performance, measure team efficiency, analyze penalty shootouts, identify comeback failures, and study how football has evolved across different eras.

---

# Dataset

The analysis is based on three datasets:

- **results.csv** – Match-level information including teams, scores, tournament, location, and match outcome.
- **goalscorers.csv** – Goal-level information including scorer, scoring minute, own goals, and penalties.
- **shootouts.csv** – Matches decided by penalty shootouts.

Since some questions require information from multiple datasets (such as shootout analysis and comeback analysis), the datasets were merged when necessary using:

- `date`
- `home_team`
- `away_team`

---

# Objectives

This analysis answers the following questions:

### 1. Top Performers
- Which national teams have scored the most goals in history?
- Who are the top international goalscorers of all time?

### 2. Team Efficiency
- Which teams earn the most points?
- Which teams score the most goals per match?
- How does applying a minimum match threshold affect the rankings?

### 3. Drama Analysis
- Which decade had the highest number of penalty shootouts?
- Which tournaments are most likely to end in penalty shootouts?

### 4. Worst Performers
- Which teams most frequently score the opening goal but still fail to win?

### 5. Era Comparison
- How have:
  - Goals per match
  - Draw rates
  - Winning margins

changed across decades since 1872?

---

# Data Preparation

The following preprocessing steps were performed:

- Converted dates to datetime format.
- Standardized historical team names.
- Handled missing values.
- Merged datasets when required for specific analyses.

---

# Feature Engineering

Several new features were created to support the analysis:

- Year
- Decade
- Total Goals
- Goal Margin
- Home Points
- Away Points
- Draw Indicator

---

# Visualizations

The notebook includes multiple visualizations such as:

- Top scoring teams
- Top international goalscorers
- Team efficiency rankings
- Penalty shootouts by decade
- Most common shootout tournaments
- Teams that score first but fail to win
- Goals per match across decades
- Draw rate across decades
- Winning margin across decades

---

# Key Findings

The analysis reveals:

- The most successful goal-scoring national teams in football history.
- The greatest international goalscorers.
- The most efficient national teams after applying a minimum match threshold.
- A steady increase in penalty shootouts over recent decades.
- Teams that frequently lose despite scoring first.
- A clear historical trend toward lower scoring matches, smaller winning margins, and higher draw rates, indicating a more balanced and competitive game.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# Insights

- England, Brazil, Germany, and Argentina remain among the most consistent high-performing national teams in terms of total goals, match points, and long-term efficiency.
- Applying a minimum match threshold provides a fairer comparison by excluding teams with very few matches that may have unusually high averages.
- Penalty shootouts have become significantly more common in modern football, with the highest frequency occurring in the 2010s.
- Friendly matches and major international tournaments account for the largest number of penalty shootouts, reflecting both experimental fixtures and high-stakes knockout competitions.
- Several teams frequently score the opening goal but still fail to win, highlighting difficulties in maintaining an early advantage and closing out matches.
- Historical analysis shows that football has become more balanced over time, with fewer goals per match, smaller winning margins, and a higher percentage of draws compared to the early decades of international football.

---

# Recommendations

- Use efficiency metrics (points per match and goals per match) alongside total statistics when evaluating national team performance.
- Always apply a minimum match threshold when comparing teams to avoid misleading rankings caused by small sample sizes.
- Coaching staffs should analyze matches where teams concede after scoring first to improve game management and defensive organization.
- Tournament organizers and analysts can use historical shootout trends to better understand the increasing importance of penalty preparation.
- Future analyses could incorporate additional variables such as FIFA rankings, home advantage, team strength, or expected goals (xG) to provide deeper performance insights.
- Building predictive models using these historical features could help forecast match outcomes and identify factors influencing team success.
