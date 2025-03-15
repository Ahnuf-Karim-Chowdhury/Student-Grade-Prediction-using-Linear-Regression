# Student Grade Prediction using Linear Regression

This project focuses on predicting students' final grades (G3) using a machine learning approach based on linear regression. The dataset consists of features like first (G1) and second (G2) period grades, study time, number of failures, and absences.

## Overview
- **Objective**: Predict the target variable `G3` (final grade).
- **Model**: Linear Regression is employed to analyze the relationships between input features and the target grade.
- **Dataset**: Data is preprocessed to include relevant features (`G1`, `G2`, `studytime`, `failures`, and `absences`) for predicting `G3`.

## Process Breakdown
1. **Dataset Preparation**:
   - Loaded and preprocessed the dataset (`student-mat.csv`).
   - Selected key features influencing student performance.
   - Split the data into training and testing sets (90%-10% split).

2. **Model Training**:
   - Trained the Linear Regression model on the training set.
   - Used multiple iterations to identify the model with the highest accuracy, saving it with `pickle`.

3. **Model Evaluation**:
   - Examined model performance through coefficients and intercept values.
   - Predicted `G3` grades based on test data and compared predictions against actual results.

4. **Visualization**:
   - Generated insightful visualizations to explore feature relationships with the target grade.

## Visual Results
Here are the graphical results demonstrating the relationship between features and final grades:

### G1 Results
![G1 Results](https://github.com/Ahnuf-Karim-Chowdhury/Student-Grade-Prediction-using-Linear-Regression/blob/main/Result%20Predictions/G1.png?raw=true)  
This graph illustrates how the grades from the first period (G1) correlate with the final grades (G3).  
- **X-axis**: First period grades (G1).  
- **Y-axis**: Final grades (G3).

### G2 Results
![G2 Results](https://github.com/Ahnuf-Karim-Chowdhury/Student-Grade-Prediction-using-Linear-Regression/blob/main/Result%20Predictions/G2.png?raw=true)  
This graph highlights the relationship between second period grades (G2) and the final grades (G3), showing a stronger linear trend compared to G1.  
- **X-axis**: Second period grades (G2).  
- **Y-axis**: Final grades (G3).

### Absences
![Absence Results](https://github.com/Ahnuf-Karim-Chowdhury/Student-Grade-Prediction-using-Linear-Regression/blob/main/Result%20Predictions/absencees.png?raw=true)  
This visualization reveals the impact of absences on final grades (G3), indicating that higher absences often lead to lower grades.  
- **X-axis**: Number of absences.  
- **Y-axis**: Final grades (G3).

### Failures
![Failures Results](https://github.com/Ahnuf-Karim-Chowdhury/Student-Grade-Prediction-using-Linear-Regression/blob/main/Result%20Predictions/failures.png?raw=true)  
This graph shows the connection between the number of past failures and the final grades (G3), illustrating a negative correlation.  
- **X-axis**: Number of past failures.  
- **Y-axis**: Final grades (G3).

### Study Time
![Study Time Results](https://github.com/Ahnuf-Karim-Chowdhury/Student-Grade-Prediction-using-Linear-Regression/blob/main/Result%20Predictions/studytime.png?raw=true)  
This plot explores how weekly study time correlates with final grades (G3), suggesting that more study time tends to result in higher grades.  
- **X-axis**: Weekly study time (1: <2 hours, 2: 2-5 hours, 3: 5-10 hours, 4: >10 hours).  
- **Y-axis**: Final grades (G3).
