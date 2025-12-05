#TITTLE: WEATHER DATA
#NAME: Muskan Nehra
#DESCRIPTION: A program that analyzes weather data from a CSV file to clean it, visualize trends, calculate statistics, and generate a summary report.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV safely
try:
    df = pd.read_csv("weather.csv")
except FileNotFoundError:
    print("❌ weather.csv not found!")
    exit()

# Check required columns
required_cols = {"date", "temperature", "humidity"}
if not required_cols.issubset(df.columns):
    print("❌ CSV must contain: date, temperature, humidity columns.")
    exit()

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Remove invalid or missing rows
df = df.dropna(subset=['date', 'temperature', 'humidity'])

# Extract month
df['month'] = df['date'].dt.month

# Monthly average
monthly_avg = df.groupby('month')['temperature'].mean()

# -----------------------------
#           PLOTS
# -----------------------------

plt.figure(figsize=(12, 8))

# 1. Line Plot
plt.subplot(3, 1, 1)
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Line Plot")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

# 2. Bar Chart
plt.subplot(3, 1, 2)
plt.bar(monthly_avg.index, monthly_avg.values)
plt.title("Average Monthly Temperature (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Avg Temp (°C)")

# 3. Scatter Plot
plt.subplot(3, 1, 3)
plt.scatter(df['temperature'], df['humidity'])
plt.title("Temperature vs Humidity (Scatter Plot)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

plt.tight_layout()
plt.savefig("weather_plots.png")
plt.show()

# -----------------------------
#      STATISTICS
# -----------------------------
temps = df['temperature'].values

report = f"""
# Weather Data Summary Report

### 📌 Temperature Statistics
- **Mean:** {np.mean(temps):.2f} °C  
- **Max:** {np.max(temps):.2f} °C  
- **Min:** {np.min(temps):.2f} °C  
- **Standard Deviation:** {np.std(temps):.2f} °C  

### 📌 Included Visuals
- Line Plot  
- Bar Chart  
- Scatter Plot  
(✔ Saved as: `weather_plots.png`)
"""

# Save report
with open("weather_report.md", "w") as file:
    file.write(report)

print("✅ Analysis complete! Plots saved as weather_plots.png and report saved as weather_report.md")
