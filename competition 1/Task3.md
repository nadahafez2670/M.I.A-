# ⚽ FIFA Player Rating Prediction

## Project Overview

The objective of this competition is to predict **player ratings** from football match statistics.

Instead of focusing only on maximizing the leaderboard score, this project followed a hypothesis-driven workflow. Every experiment was designed to answer a specific question about the data or the model's behavior.

The final solution combines **LightGBM** and **CatBoost** using simple blending after multiple rounds of experimentation, feature engineering, and error analysis.

---

# Workflow

## 1. Exploratory Data Analysis (EDA)

The first step was understanding the dataset before building any model.

The following analyses were performed:

- Data types
- Missing values
- Duplicate records
- Target distribution
- Feature distributions
- Correlation analysis
- Potential data leakage inspection

### Main Observations

- Most player ratings are concentrated around the middle values.
- A large number of features are highly sparse.
- Some engineered competition features were strongly correlated with the target.
- The target distribution suggested that predicting extreme ratings could be challenging.

---
# 2. Data Preprocessing

Before training any model, the dataset was preprocessed to ensure a consistent and reproducible machine learning pipeline.

The preprocessing pipeline was implemented using **scikit-learn's ColumnTransformer** and **Pipeline**, allowing the same transformations to be applied during both training and inference.

# Data Cleaning

Before training the models, the dataset was cleaned and inspected to ensure reliable results.
During the EDA, `performance_score` showed an extremely high correlation with the target (`player_rating`), indicating that it likely contained information directly derived from or highly related to the target.

Although keeping this feature significantly improved the validation and leaderboard scores, it was intentionally removed to avoid data leakage and ensure that the final model learned from legitimate match statistics rather than indirectly using the target itself.

### Numerical Features

Numerical features were:

- Imputed using the median to handle missing values.
- Left unscaled since tree-based models (LightGBM and CatBoost) do not require feature scaling.

### Categorical Features

Categorical variables were encoded using **One-Hot Encoding**, allowing the models to learn category-specific patterns without introducing ordinal relationships.

The encoder was configured to ignore unseen categories during inference.

### Why a Pipeline?

Using a preprocessing pipeline provided several advantages:

- Prevented data leakage.
- Guaranteed identical preprocessing for training, validation, and test data.
- Simplified experimentation with different models.
- Made the final solution reproducible.

# 3. Baseline Models

Several machine learning models were trained to determine the most suitable algorithm.

Models explored:

- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost

### Observation

Gradient Boosting models consistently outperformed the remaining algorithms.

LightGBM and CatBoost achieved the strongest validation performance and became the focus of the remaining experiments.

---

# 4. Hyperparameter Tuning

After selecting LightGBM, several tuning strategies were explored.

### Manual Tuning

The following parameters were adjusted manually:

- learning_rate
- n_estimators
- num_leaves
- max_depth
- subsample
- colsample_bytree

---

### RandomizedSearchCV

A Randomized Search was also performed to automatically explore different parameter combinations.

The search included parameters such as:

- learning_rate
- n_estimators
- num_leaves
- max_depth
- min_child_samples
- subsample
- colsample_bytree
- reg_alpha
- reg_lambda

### Observation

RandomizedSearchCV produced validation scores that were extremely close to the manually tuned model.

The improvement was negligible and did not justify the additional computational cost.

Therefore, the manually tuned configuration was retained as the final LightGBM model.

This suggested that the model performance was no longer limited by hyperparameter tuning, but rather by the information contained in the available features.

---

# 5. Error Analysis

Since tuning produced only marginal improvements, the focus shifted toward understanding **why the model makes mistakes**.

The following analyses were performed:

- Predicted vs True Ratings
- Residual plots
- Largest prediction errors
- Error grouped by player position
- Comparison between hard and easy predictions

---

## Main Finding — Regression Toward the Mean

The strongest observation was that the model tends to predict values close to the average rating.

This phenomenon is known as **Regression Toward the Mean**.

The model frequently:

- Overestimates low-rated performances.
- Underestimates exceptional performances.

Instead of predicting extreme ratings, predictions were pulled toward the center of the distribution.

This became the main motivation for the following feature engineering stage.

---

# 6. Feature Engineering

The error analysis suggested that many raw match statistics were affected by playing time.

For example:

Two players may complete the same number of passes.

- Player A played 90 minutes.
- Player B played only 30 minutes.

Although the totals are identical, their actual performance is clearly different.

Therefore, efficiency-based features were introduced.

### New Features

- `distance_per_min`
- `passes_per_min`
- `def_actions_per_min`

These features normalize player actions by playing time and better represent player efficiency rather than raw totals.

---

# 7. Additional Experiments

Several hypotheses were tested during the project.

## Removing Potential Leakage

A highly correlated feature (`performance_score`) was removed because it appeared to encode information extremely close to the target.

Although it substantially improved the leaderboard score, it was intentionally excluded to avoid data leakage.

---

## Target Transformation

The target distribution was investigated to determine whether a mathematical transformation could improve model performance.

Since LightGBM and CatBoost naturally handle skewed regression targets, no consistent improvement was observed.

The original target was therefore retained.

---

## Sample Weighting

Because the model struggled with extreme ratings, sample weighting was tested to give larger importance to difficult examples.

Although the idea was theoretically reasonable, it did not produce a consistent improvement on the validation set, so it was discarded.

---

## Different Feature Engineering Ideas

Several additional engineered features were explored.

Some produced little or no improvement and were removed from the final pipeline.

Only the features that consistently improved validation performance were kept.

---

# 8. Final Model

The final solution combines two Gradient Boosting models.

- LightGBM
- CatBoost

Final prediction:

```python
final_prediction = 0.5 * lgb_prediction + 0.5 * cat_prediction
```

Simple averaging produced slightly better leaderboard performance than either individual model.

---

# Final Results

## Best Public Leaderboard Score

**0.22942**

This score was achieved after combining:

- Careful EDA
- Multiple baseline models
- Hyperparameter tuning
- Error analysis
- Feature engineering
- LightGBM
- CatBoost
- Model blending

rather than relying solely on model tuning.

---

# Lessons Learned

The largest improvements came from understanding:

- why the model fails,
- where prediction errors occur,
- how player statistics should be represented,
- and which engineered features better capture player performance.

This project reinforced the importance of **data understanding**, **error analysis**, and **feature engineering** in building high-performing machine learning models.