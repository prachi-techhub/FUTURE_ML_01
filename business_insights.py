import pandas as pd
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_DIR / "outputs"

FORECAST_PATH = OUTPUT_DIR / "future_sales_forecast.csv"

# Load forecast data
df = pd.read_csv(FORECAST_PATH)

df["Month"] = pd.to_datetime(df["Month"])

# Calculate business insights
total_sales = df["Predicted_Sales"].sum()

average_sales = df["Predicted_Sales"].mean()

highest_sales = df["Predicted_Sales"].max()

lowest_sales = df["Predicted_Sales"].min()

best_month = df.loc[
    df["Predicted_Sales"].idxmax(), "Month"
]

worst_month = df.loc[
    df["Predicted_Sales"].idxmin(), "Month"
]

# Display results
print("\n========== BUSINESS INSIGHTS ==========")

print(f"\nTotal Forecasted Sales: {total_sales:,.2f}")

print(f"Average Monthly Sales: {average_sales:,.2f}")

print(f"Highest Predicted Sales: {highest_sales:,.2f}")

print(f"Lowest Predicted Sales: {lowest_sales:,.2f}")

print(f"Best Sales Month: {best_month.strftime('%B %Y')}")

print(f"Weakest Sales Month: {worst_month.strftime('%B %Y')}")

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print("""
1. INVENTORY PLANNING:
   Maintain sufficient stock before months
   with higher predicted sales.

2. STAFF MANAGEMENT:
   Arrange additional staff during expected
   high-demand periods.

3. FINANCIAL PLANNING:
   Use forecasted revenue estimates to
   prepare monthly budgets.

4. AVOID OVERSTOCKING:
   Reduce unnecessary inventory during
   expected low-sales periods.

5. BUSINESS STRATEGY:
   Monitor actual sales and compare them
   with predicted sales every month.
""")

print("\nBusiness insights generated successfully!")