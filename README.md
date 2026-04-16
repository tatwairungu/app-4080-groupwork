VERSION CONTROL SYSTEM PRACTICAL ASSIGNMENT

Introduction

This project demonstrates the application of version control concepts in the development and evaluation of machine learning models. It focuses on collaborative software development using Git and GitHub, as well as the implementation and comparison of multiple classification models for fraud detection.

Through this assignment, we demonstrate the ability to clone, modify, and manage code within a distributed version control system. The project also highlights key collaborative workflows such as branching, committing, merging, and resolving conflicts.

⸻

Project Overview

The objective of this project is to detect fraudulent transactions using a supply chain dataset. Three machine learning models were implemented and compared:
	•	Support Vector Machine (SVM)
	•	Decision Tree Classifier
	•	Random Forest Classifier

Each model was trained and evaluated using the same dataset to ensure a fair comparison.

⸻

Objectives
	•	Apply version control concepts using Git and GitHub
	•	Collaborate using branches and merge workflows
	•	Implement multiple machine learning models
	•	Evaluate model performance using standard metrics
	•	Compare models to determine the most suitable for fraud detection

⸻

Technologies Used
	•	Python
	•	Pandas
	•	Scikit-learn
	•	Matplotlib / Seaborn
	•	Git
	•	GitHub

⸻

Dataset

The project uses the DataCo Smart Supply Chain dataset, which includes:
	•	Customer information
	•	Order details
	•	Product data
	•	Delivery and transaction attributes

The dataset was preprocessed through cleaning, feature engineering, and encoding before model training.

⸻

Version Control Workflow

The project followed a collaborative GitHub workflow:
	•	Repository created on GitHub
	•	Each member worked on a separate branch:
	•	feature/svm-model
	•	feature/decision-tree
	•	feature/random-forest
	•	Changes were committed with clear messages
	•	Branches were pushed to the remote repository
	•	Pull requests were used to merge work into the main branch
	•	Merge conflicts were identified and resolved during integration

This workflow ensured organized collaboration and proper version tracking.

⸻

Model Performance (Fraud Detection)

SVM
Accuracy - 97.75%
Recall - 56.69%
F1 Score - 28.40%

Decision Tree
Accuracy - 99.10%
Recall - 79.65%
F1 score - 80.64%

Random Forest
Accuracy - 98.71%
Recall - 45.65%
F1 score - 62.53%

Results Summary

The Decision Tree model achieved the best performance overall, with the highest recall and F1-score. This indicates that it was more effective at identifying fraudulent transactions while maintaining a good balance between precision and recall.

The Random Forest model performed well but showed lower recall compared to Decision Tree. The SVM model achieved high accuracy but struggled to detect fraudulent cases effectively.

⸻

Conclusion

This project shows that combining machine learning with version control practices improves both technical outcomes and team collaboration. GitHub enabled efficient teamwork, while the comparison of models provided insights into selecting the most suitable algorithm for fraud detection.

⸻

Future Improvements
	•	Tune model hyperparameters for better performance
	•	Address class imbalance using techniques such as SMOTE
	•	Explore additional machine learning models
	•	Deploy the model for real-time fraud detection
