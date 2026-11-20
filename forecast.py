import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from pathlib import Path

# =====================================
# 1. Set project paths
# =====================================

PROJECT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_DIR / "outputs"

MODEL_PATH = OUTPUT_DIR / "sales_forecast_model.joblib"

# =====================================
# 2. Load trained model
# =====================================

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
FEATURES = saved_data["features"]

last_time_index = saved_data["last_time_index"]
last_month = pd.Timestamp(saved_data["last_month"])

print("Trained model loaded successfully!")

# =====================================
# 3. Generate next 6 months
# =====================================

future_dates = pd.date_range(
    start=last_month + pd.DateOffset(months=1),
    periods=6,
    freq="MS"
)

# =====================================
# 4. Create future time features
# =====================================

future_df = pd.DataFrame({
    "Month": future_dates
})

future_df["Year"] = future_df["Month"].dt.year

future_df["Month_Number"] = (
    future_df["Month"].dt.month
)

future_df["Time_Index"] = np.arange(
    last_time_index + 1,
    last_time_index + 7
)

future_df["Month_Sin"] = np.sin(
    2 * np.pi * future_df["Month_Number"] / 12
)

future_df["Month_Cos"] = np.cos(
    2 * np.pi * future_df["Month_Number"] / 12
)

# =====================================
# 5. Predict future sales
# =====================================

X_future = future_df[FEATURES]

future_predictions = model.predict(X_future)

future_df["Predicted_Sales"] = future_predictions

# =====================================
# 6. Display forecast
# =====================================

print("\nNEXT 6 MONTHS SALES FORECAST")
print("--------------------------------")

print(
    future_df[
        ["Month", "Predicted_Sales"]
    ].to_string(index=False)
)

# =====================================
# 7. Save forecast results
# =====================================

forecast_path = OUTPUT_DIR / "future_sales_forecast.csv"

future_df[
    ["Month", "Predicted_Sales"]
].to_csv(forecast_path, index=False)

print("\nForecast saved successfully!")

# =====================================
# 8. Create forecast graph
# =====================================

plt.figure(figsize=(12, 6))

plt.plot(
    future_df["Month"],
    future_df["Predicted_Sales"],
    marker="o",
    linewidth=2,
    label="Predicted Sales"
)

plt.title("Future Sales Forecast - Next 6 Months")

plt.xlabel("Month")

plt.ylabel("Predicted Sales")

plt.legend()

plt.grid(True, alpha=0.3)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "future_sales_forecast.png",
    dpi=300
)

plt.show()

print("\nFuture sales forecasting completed!")