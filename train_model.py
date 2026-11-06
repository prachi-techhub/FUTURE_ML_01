import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# =====================================
# 1. Set project paths
# =====================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "outputs"

DATA_PATH = OUTPUT_DIR / "monthly_sales.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =====================================
# 2. Load monthly sales data
# =====================================

df = pd.read_csv(DATA_PATH)

df["Month"] = pd.to_datetime(df["Month"])
df = df.sort_values("Month").reset_index(drop=True)

print("Monthly sales data loaded successfully!")
print(df.head())

# =====================================
# 3. Create time-based features
# =====================================

df["Year"] = df["Month"].dt.year
df["Month_Number"] = df["Month"].dt.month

# Number of months since the beginning
df["Time_Index"] = np.arange(len(df))

# Cyclical features to represent seasonal patterns
df["Month_Sin"] = np.sin(
    2 * np.pi * df["Month_Number"] / 12
)

df["Month_Cos"] = np.cos(
    2 * np.pi * df["Month_Number"] / 12
)

FEATURES = [
    "Time_Index",
    "Month_Number",
    "Year",
    "Month_Sin",
    "Month_Cos"
]

X = df[FEATURES]
y = df["Sales"]

# =====================================
# 4. Split data chronologically
# =====================================

if len(df) < 12:
    raise ValueError(
        "At least 12 monthly observations are recommended "
        "for this forecasting experiment."
    )

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nTraining observations:", len(X_train))
print("Testing observations:", len(X_test))

# =====================================
# 5. Train the model
# =====================================

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=5,
    min_samples_leaf=2,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel training completed!")

# =====================================
# 6. Predict test-period sales
# =====================================

predictions = model.predict(X_test)

# =====================================
# 7. Evaluate model performance
# =====================================

mae = mean_absolute_error(y_test, predictions)

rmse = np.sqrt(
    mean_squared_error(y_test, predictions)
)

# Compare against a simple historical-average baseline
baseline_predictions = np.full(
    len(y_test),
    y_train.mean()
)

baseline_mae = mean_absolute_error(
    y_test,
    baseline_predictions
)

print("\nMODEL EVALUATION")
print("------------------------------")
print(f"Model MAE:     {mae:.2f}")
print(f"Model RMSE:    {rmse:.2f}")
print(f"Baseline MAE:  {baseline_mae:.2f}")

# =====================================
# 8. Save test predictions
# =====================================

results = pd.DataFrame({
    "Month": df["Month"].iloc[split_index:].values,
    "Actual_Sales": y_test.values,
    "Predicted_Sales": predictions
})

results.to_csv(
    OUTPUT_DIR / "model_evaluation.csv",
    index=False
)

# =====================================
# 9. Visualize actual vs predicted
# =====================================

plt.figure(figsize=(12, 6))

plt.plot(
    results["Month"],
    results["Actual_Sales"],
    marker="o",
    label="Actual Sales"
)

plt.plot(
    results["Month"],
    results["Predicted_Sales"],
    marker="o",
    linestyle="--",
    label="Predicted Sales"
)

plt.title("Actual vs Predicted Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "model_evaluation.png",
    dpi=300
)

plt.show()

# =====================================
# 10. Save trained model
# =====================================

joblib.dump(
    {
        "model": model,
        "features": FEATURES,
        "last_time_index": len(df) - 1,
        "last_month": df["Month"].max()
    },
    OUTPUT_DIR / "sales_forecast_model.joblib"
)

print("\nModel saved successfully!")
print("Check the outputs folder for the results.")