# Task 2.3 – The Scouting Engine: Finding Mohamed Salah's Successor

## Overview

The objective of this task is to build a player similarity search engine using the FIFA 19 Complete Player Dataset. The system identifies players with playing profiles most similar to Mohamed Salah by representing each player as a feature vector and comparing them using multiple similarity metrics implemented from scratch with NumPy.

---

## Dataset

The same FIFA 19 dataset from Task 2.2 was used.

### Selected Features

- Finishing
- ShortPassing
- Dribbling
- SprintSpeed
- Strength
- Stamina
- Interceptions
- StandingTackle
- Value

---

## Data Preprocessing

Before computing similarities, the selected features were standardized using Z-score normalization:

\[
z=\frac{x-\mu}{\sigma}
\]

This ensures that all features contribute equally regardless of their original scale.

A comparison was also performed using the raw (unstandardized) data to illustrate the importance of feature scaling.

---

## Similarity Metrics

Three similarity measures were implemented manually using NumPy.

### 1. Euclidean Distance

Measures the straight-line distance between two player vectors.

\[
d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
\]

Smaller values indicate greater similarity.

---

### 2. Manhattan Distance

Measures the total absolute difference between two player vectors.

\[
d(x,y)=\sum_{i=1}^{n}|x_i-y_i|
\]

Smaller values indicate greater similarity.

---

### 3. Cosine Similarity

Measures the similarity of the direction of two vectors regardless of their magnitude.

\[
\cos(\theta)=\frac{x\cdot y}{||x||\,||y||}
\]

Larger values (closer to 1) indicate greater similarity.

---

## Standardized vs. Raw Features

Without standardization, the **Value** feature dominates the similarity calculations because its numerical scale is much larger than the remaining attributes.

After standardization, each feature contributes equally, producing more meaningful similarity recommendations.

---

## Similarity Results

The three metrics produced highly consistent recommendations. The most frequently recommended players were:

- Antoine Griezmann
- Kylian Mbappé
- Philippe Coutinho
- James Rodríguez
- Leroy Sané

Although the ranking changes slightly between metrics, the overall shortlist remains largely consistent.

---

## PCA Validation

To validate the similarity search, the custom PCA implementation developed in Task 2.2 was reused.

All players were projected onto the first two principal components.

- All players were displayed in grey.
- Mohamed Salah was highlighted with a blue star.
- The final recommended players were highlighted in red.

The visualization shows that the recommended players occupy the same general region of the PCA space as Mohamed Salah, providing visual confirmation that the similarity search is meaningful.

---

## Conclusion

A complete player similarity search engine was developed using custom NumPy implementations of Euclidean Distance, Manhattan Distance, and Cosine Similarity.

The experiment demonstrates that feature standardization is essential for fair similarity comparisons, while the PCA visualization provides an additional qualitative validation of the final scouting recommendations.