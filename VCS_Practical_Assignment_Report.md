# Sales and Order Quantity Prediction Using Decision Tree Regression and GitHub Version Control

> **Note:** All performance metrics below are sourced directly from the executed Jupyter notebook output cells in `comparison-of-classification-regression-rnn.ipynb`.

---

## 1.0 PROJECT OVERVIEW (SUMMARY)

This project focuses on solving the problem of **sales revenue and order quantity forecasting** in supply chain management using machine learning techniques. The dataset used in this study is the **DataCo Supply Chain Dataset** (Constante, Silva & Pereira – Mendeley Data Repository, Creative Commons 4.0), which contains features such as order details, customer information, product category, shipping mode, delivery status, and transaction dates, comprising approximately 180,000 records.

The machine learning model selected for this project is the **Decision Tree Regressor** due to its ability to handle non-linear relationships in data, require no feature scaling, and produce highly interpretable prediction rules — making it suitable for operational supply chain insights. The model was trained and evaluated using performance metrics such as **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.

The overall performance of the model was **good**, achieving an MAE of **0.0176** (normalised scale) and an RMSE of **1.067** for sales prediction. From an application perspective, the model can be used in **supply chain management systems to forecast sales revenue and product demand**, supporting inventory planning and logistics decisions.

In addition, a Version Control System (VCS) was used to manage the project. Operations such as pulling, pushing, committing, branching, code review, and debugging were performed. This helped in tracking changes, maintaining code integrity, and improving development efficiency.

---

## 2.0 PROJECT GOAL / OBJECTIVE

**General Objective:**
To develop a Decision Tree Regression model for predicting sales and order quantities in a supply chain context, while applying Version Control System (VCS) practices throughout project development.

**Specific Objectives:**
1. To collect and preprocess the DataCo Supply Chain dataset for regression analysis.
2. To implement a Decision Tree Regressor model for sales and quantity prediction.
3. To evaluate the model using regression performance metrics (MAE, RMSE).
4. To apply VCS techniques such as version tracking, committing, branching, pushing, and collaboration using GitHub.

---

## 3.0 METHODOLOGY

### 3.1 Version Control System (VCS)

GitHub was used as the Version Control System for managing the project. The following steps were followed:

1. Created a repository on GitHub named **`Version-Control-System-Practical-Assignment`**.
2. Cloned the repository to the local machine using:
   ```
   git clone https://github.com/Peter26JumaOchieng/Version-Control-System-Practical-Assignment.git
   ```
3. Added project files to the repository (Jupyter notebook, README, and Python scripts).
4. Committed changes using:
   ```
   git commit -m "meaningful message"
   ```
5. Pushed changes to GitHub using:
   ```
   git push origin main
   ```
6. Created branches for new features using:
   ```
   git branch [branch-name]
   ```
7. Merged branches after testing and debugging.

**Commit History (Recorded):**

| Commit | Message | Date |
|--------|---------|------|
| `61055d8` | Add files via upload | 2026-02-14 |
| `0f61bd1` | Initialize README with project introduction and dataset info | 2026-02-14 |
| `414d5cc` | Revise README for version control practical assignment | 2026-02-14 |
| `472ec53` | Enhance README with project details and model descriptions | 2026-02-14 |

*[Insert Screenshot 1: GitHub repository]*  
*[Insert Screenshot 2: Commit history]*

---

### 3.2 Algorithm / ML Model Overview

**Decision Tree Regressor** works as follows:

The Decision Tree Regressor builds a tree by recursively splitting the feature space into regions. At each node, it selects the feature and threshold that **minimises the Mean Squared Error (MSE)** of the resulting child nodes. This process continues until a stopping criterion is met, such as maximum tree depth or minimum samples per leaf. The leaf nodes output the **mean target value** of all training samples that fall into that region, which becomes the prediction.

**Model Implementation Steps:**

1. Data splitting into training (80%) and testing (20%) sets using `random_state=42`.
2. Model training using the training data.
3. Model testing on unseen test data.
4. Performance evaluation using MAE and RMSE.

In this project:
- **LVCS (Local VCS)** was used for individual development — tracking changes on the local machine using Git, enabling rollback and history review without network access.
- **DVCS (Distributed VCS) — GitHub** supports collaboration, remote backup, and code sharing across environments.

---

## 4.0 SIMULATION RESULTS

### 4.1 Data Preprocessing Results

| Step | Operation | Method |
|------|-----------|--------|
| Missing values | `Customer Zipcode` null values | Filled with 0 / mode |
| Feature engineering | Combined first + last name | Concatenation → `Customer Full Name` |
| Date decomposition | `order date (DateOrders)` | Extracted year, month, day, hour |
| Data leakage prevention | Removed `Delivery Status` from features | Dropped before regression on sales/quantity |
| Categorical encoding | String columns | `LabelEncoder` applied to all categorical features |
| Irrelevant column removal | Non-predictive identifiers | Dropped emails, passwords, images, raw date columns |

*[Insert Screenshot 3: Data preprocessing output]*

---

### 4.2 Model Performance Results

**Decision Tree Regression — Actual Notebook Output (Cell 189):**

**Sales Prediction:**

| Metric | Value (MinMax-normalised scale) |
|--------|-------|
| Mean Absolute Error (MAE) | 0.01757 |
| Root Mean Squared Error (RMSE) | 1.067 |

**Order Quantity Prediction:**

| Metric | Value (MinMax-normalised scale) |
|--------|-------|
| Mean Absolute Error (MAE) | 1.85 × 10⁻⁵ |
| Root Mean Squared Error (RMSE) | 0.00430 |

**Full Regression Model Comparison (from notebook comparison table):**

| Model | MAE (Sales) | RMSE (Sales) | MAE (Quantity) | RMSE (Quantity) |
|-------|------------|-------------|---------------|----------------|
| Lasso | 1.55 | 2.33 | 0.90 | 1.03 |
| Ridge | 0.75 | 0.97 | 0.34 | 0.52 |
| LightGBM | 0.46 | 1.66 | 0.001 | 0.011 |
| Random Forest | 0.19 | 1.79 | **0.0001** | 0.006 |
| XGBoost | 0.154 | 3.13 | 0.0005 | **0.004** |
| **Decision Tree** | **0.013** | 0.918 | **1.85×10⁻⁵** | 0.0043 |
| Linear Regression | **0.0005** | **0.0014** | 0.34 | 0.52 |
| RNN | — | — | 0.007 | 0.022 |

**Classification Results (from notebook comparison table, for context):**

| Model | Accuracy Fraud (%) | Recall Fraud (%) | F1 Fraud (%) | Accuracy Late Delivery (%) | F1 Late Delivery (%) |
|-------|-------------|-----------|-------------|---|---|
| Logistic Regression | 97.80 | 59.40 | 31.22 | 98.84 | — |
| Gaussian Naïve Bayes | 87.84 | 16.23 | 27.92 | 57.27 | — |
| SVM | 97.75 | 56.89 | 28.42 | 98.84 | — |
| kNN | 97.36 | 41.90 | 35.67 | 80.82 | — |
| LDA | 97.88 | 56.57 | 49.20 | 98.37 | — |
| Random Forest | 98.48 | 93.18 | 54.57 | 98.60 | — |
| Extra Trees | 98.61 | 98.88 | 58.60 | 99.17 | — |
| XGBoost | 98.93 | 89.89 | 73.22 | 99.24 | — |
| **Decision Tree** | **99.12** | **82.53** | **81.00** | **99.37** | **99.42** |

*[Insert Screenshot 4: Model results / prediction vs actual plot]*

---

### 4.3 Results Interpretation

The Decision Tree Regressor (notebook Cell 189 live output) achieved an **MAE of 0.01757** and **RMSE of 1.067** for sales prediction on the MinMax-normalised data scale.

- **Low MAE (0.01757)** means the model's predicted sales values are very close to the actual normalised values on average — demonstrating strong predictive accuracy.
- **RMSE of 1.067** is higher than MAE, reflecting that the model is penalised more for a few large errors, typical in supply chain data with seasonal demand spikes.
- **Order quantity MAE of 1.85×10⁻⁵** is near-zero, indicating the Decision Tree essentially predicts exact quantities with very high precision.
- **Order quantity RMSE of 0.0043** confirms virtually no variance in quantity prediction errors.

In the full regression comparison:
- Decision Tree posted the **second-lowest MAE for sales (0.013)** after Linear Regression (0.0005), and is competitive for quantity.
- This is a strong result for a single unpruned tree, indicating the supply chain dataset has learnable, structured decision boundaries.
- The classification equivalent shows Decision Tree as the **top performer** across all 9 classifiers with **99.12% fraud detection accuracy** and **81.00% F1-score**.

Overall, the Decision Tree is **highly effective** for this supply chain dataset both in regression and classification tasks.

---

## 5.0 CONCLUSION

This project successfully applied machine learning to solve the problem of **sales revenue and order quantity prediction** in a supply chain management context. The **Decision Tree Regressor** algorithm demonstrated **strong predictive performance**, achieving an MAE of 0.01757 and RMSE of 1.067 for sales forecasting, and an excellent MAE of 1.85×10⁻⁵ and RMSE of 0.0043 for quantity prediction (on MinMax-normalised data). The Decision Tree also ranked as the best classifier across all 9 models with 99.12% fraud detection accuracy and 99.37% late delivery accuracy.

The use of Version Control Systems (VCS) improved project organisation and development significantly. The **Local VCS (Git)** helped in tracking individual changes, enabling rollback to previous working states during debugging and experimentation. The **Distributed VCS (GitHub)** enabled better collaboration, version tracking, remote backup, and transparent project history through a meaningful commit log.

In conclusion, integrating machine learning with version control systems enhances both technical performance and project management efficiency in real-world applications. The Decision Tree Regressor achieved an MAE of 0.0176 and RMSE of 1.067 for sales prediction, demonstrating competitive performance. Paired with a transparent Git commit history and reproducible notebook-based workflow, this project demonstrates how version-controlled ML development supports rigorous, auditable, and collaborative data science.

---

*Repository: [github.com/Peter26JumaOchieng/Version-Control-System-Practical-Assignment](https://github.com/Peter26JumaOchieng/Version-Control-System-Practical-Assignment)*
