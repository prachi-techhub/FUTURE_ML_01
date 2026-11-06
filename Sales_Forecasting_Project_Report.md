# SALES FORECASTING SYSTEM USING MACHINE LEARNING

## 1. Introduction

Sales forecasting is an important process in business that helps organizations estimate future sales using historical data.

This project develops a Machine Learning-based Sales Forecasting System using the Superstore Sales Dataset.

The system analyzes historical sales records, identifies monthly sales patterns and predicts future sales for the next six months.

## 2. Problem Statement

Businesses often face difficulties estimating future sales. Incorrect predictions can lead to overstocking, product shortages, financial losses and poor resource management.

This project aims to solve this problem by using historical sales data and Machine Learning techniques to generate future sales predictions.

## 3. Objectives

- Analyze historical sales data.
- Clean and preprocess the dataset.
- Identify monthly sales trends.
- Apply time-based feature engineering.
- Develop a Machine Learning forecasting model.
- Evaluate model performance.
- Predict sales for the next six months.
- Generate useful business recommendations.

## 4. Dataset Description

Dataset Name: Superstore Sales Dataset.

The dataset contains historical retail sales information, including:

- Order ID
- Order Date
- Ship Date
- Customer Information
- Product Category
- Region
- Sales
- Profit
- Quantity

The dataset is used to understand historical sales patterns and forecast future sales.

## 5. Tools and Technologies

**Programming Language:** Python

**Libraries:**
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

**Development Environment:**
- Visual Studio Code
- Python Virtual Environment

## 6. Data Preprocessing

Data preprocessing prepares raw data for Machine Learning.

The project includes:
- Loading the Superstore dataset.
- Handling missing values.
- Removing duplicate records.
- Converting order dates into datetime format.
- Grouping sales data by month.
- Preparing monthly sales information.

## 7. Exploratory Data Analysis

Monthly sales analysis is performed to understand historical sales patterns.

A line graph is generated to visualize monthly sales trends.

This helps identify changes in sales over time and understand potential seasonal patterns.

## 8. Feature Engineering

Time-based features are created to help the model understand the relationship between time and sales.

The features include:

- Year
- Month Number
- Time Index
- Month Sin
- Month Cos

Cyclical features help represent the repeating nature of months throughout the year.

## 9. Machine Learning Algorithm

The project uses the Random Forest Regressor algorithm.

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to generate predictions.

It is used to estimate future monthly sales based on historical time-based features.

## 10. Model Training

The monthly sales dataset is divided chronologically into training and testing datasets.

The training dataset is used to train the model, while the testing dataset evaluates its performance on later observations.

The trained model is saved using the Joblib library for future predictions.

## 11. Model Evaluation

The model is evaluated using:

**Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted sales.

**Root Mean Squared Error (RMSE):** Measures prediction errors while giving greater weight to larger errors.

The model is also compared against a historical-average baseline.

The evaluation results are saved in a CSV file and visualized using a graph.

## 12. Future Sales Forecasting

The trained model predicts monthly sales for the next six months.

The forecast results are stored in:

- future_sales_forecast.csv
- future_sales_forecast.png

A line graph displays the predicted sales values for the upcoming six months.

## 13. Business Insights and Applications

The forecasting system can support business decisions in several ways.

**Inventory Planning:** Businesses can prepare stock according to expected sales.

**Financial Planning:** Forecasted sales can help businesses estimate future revenue.

**Staff Management:** Businesses can plan staffing requirements according to expected demand.

**Avoiding Overstocking:** Lower predicted sales can help businesses avoid unnecessary inventory.

**Business Decision-Making:** Historical trends and forecasts can support future planning.

## 14. Project Outputs

The project generates:

- Monthly sales dataset.
- Historical monthly sales visualization.
- Actual versus predicted sales visualization.
- Model evaluation results.
- Trained Machine Learning model.
- Six-month future sales predictions.
- Business insights and recommendations.

## 15. Conclusion

The Sales Forecasting System demonstrates how Machine Learning can support real-world business decisions.

By analyzing historical Superstore sales data, the system generates future sales predictions and provides useful insights for inventory planning, financial management and business strategy.

This project provides practical experience in data preprocessing, feature engineering, Machine Learning, model evaluation and data visualization.

## 16. Future Scope

The project can be improved by:

- Comparing different forecasting algorithms.
- Developing an interactive dashboard.
- Adding product-wise sales forecasting.
- Adding region-wise sales predictions.
- Improving forecasting accuracy.
- Updating predictions with new sales data.

---

**Project Title:** Sales Forecasting System Using Machine Learning

**Internship Task:** Task 1 – Sales/Demand Forecasting