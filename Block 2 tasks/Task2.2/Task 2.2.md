# Task 2.2 - Finding the Key Factors Behind Football Player Performance with PCA

## Overview

This project implements **Principal Component Analysis (PCA)** from scratch using **NumPy**, without relying on pre-built PCA implementations such as `sklearn.decomposition.PCA`.

The objective is to reduce the dimensionality of FIFA 19 player statistics while preserving as much information as possible. PCA is used to discover the main performance dimensions that distinguish football players based on their technical and physical attributes.

---

# Dataset

**Dataset:** FIFA 19 Complete Player Dataset

The following numerical features were selected for the analysis:

- Finishing
- ShortPassing
- Dribbling
- SprintSpeed
- Strength
- Stamina
- Interceptions
- StandingTackle
- Value

The **Position** column was stored separately and later used only for visualization.

---

# Data Preprocessing

The preprocessing stage included:

- Selecting the required features.
- Parsing the **Value** column from text (e.g. €110.5M) into numerical values.
- Removing rows containing missing values.
- Keeping the Position column separately for visualization.

After preprocessing, the final dataset contained:

- **18,147 players**
- **9 numerical features**

---

# PCA Implementation

The PCA algorithm was implemented manually following the standard mathematical pipeline.

### Step 1 — Standardization

Each feature was standardized using the Z-score equation:

\[
z = \frac{x-\mu}{\sigma}
\]

This ensures that every feature has:

- Mean ≈ 0
- Standard deviation ≈ 1

---

### Step 2 — Covariance Matrix

A covariance matrix was calculated from the standardized dataset.

The matrix revealed several strong relationships between variables, including:

- Interceptions ↔ StandingTackle
- ShortPassing ↔ Dribbling
- Finishing ↔ Dribbling

These correlations indicate that multiple features contain overlapping information.

---

### Step 3 — Eigen-Decomposition

The covariance matrix was decomposed into:

- Eigenvalues
- Eigenvectors

The eigenvectors define the directions of maximum variance, while the eigenvalues measure how much variance each direction explains.

---

### Step 4 — Explained Variance

The explained variance ratios were computed for all principal components.

The first principal component explains approximately **48%** of the total variance.

The first two principal components together explain approximately **70%** of the total variance.

Therefore, the first two components were selected for visualization.

---

### Step 5 — Data Projection

The standardized dataset was projected onto the first two principal components.

This transformed every player from a **9-dimensional feature space** into a **2-dimensional representation** consisting of:

- PC1
- PC2

---

# Visualization

Players were visualized using the first two principal components.

Each point represents a player and is colored according to the original **Position** column.

### Observations

- Goalkeepers (GK) form a clearly separated cluster from the rest of the players.
- Most outfield positions overlap because many positions share similar technical and physical characteristics.
- PCA is an unsupervised learning technique and therefore does not use player positions while computing the principal components.
- Despite reducing the data from nine dimensions to two, the visualization preserves approximately **70%** of the original variance.

---

# Interpretation of the Principal Components

The loading matrix was used to interpret the meaning of each principal component.

### Principal Component 1 (PC1)

PC1 receives strong positive contributions from:

- ShortPassing
- Dribbling
- Stamina
- SprintSpeed
- Finishing

This component represents the player's overall technical and physical quality.

### Principal Component 2 (PC2)

PC2 contrasts attacking attributes with defensive attributes.

Positive contributions include:

- Finishing
- Dribbling
- SprintSpeed

Negative contributions include:

- Interceptions
- StandingTackle
- Strength

Therefore, PC2 can be interpreted as an **Attacking vs Defensive Playing Style** axis.

---

# Conclusion

The PCA implementation successfully reduced the dimensionality of the FIFA 19 player dataset while preserving most of its important information.

The visualization demonstrates that:

- Goalkeepers possess clearly distinct characteristics.
- Many outfield positions naturally overlap due to similar playing styles.
- PCA effectively captures the major patterns in player performance using only two principal components.

---

# Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---
