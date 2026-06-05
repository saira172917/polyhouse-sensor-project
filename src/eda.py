import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load data
df = pd.read_parquet("data/interim/02_cleaned.parquet")

# ----------------------------
# 1. DATA QUALITY REPORT
# ----------------------------
summary = df[["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]].describe().T
summary["cv"] = summary["std"] / summary["mean"]

report = []
report.append("# Polyhouse Data Quality Report\n")
report.append(f"Rows: {len(df)}")
report.append(f"Date range: {df['timestamp'].min()} → {df['timestamp'].max()}\n")
report.append(summary.to_markdown())

Path("reports").mkdir(exist_ok=True)
Path("reports/data_quality.md").write_text("\n".join(report), encoding="utf-8")

# ----------------------------
# 2. CREATE FIGURE FOLDER
# ----------------------------
Path("reports/figures").mkdir(parents=True, exist_ok=True)

# ----------------------------
# 3. CORRELATION HEATMAP
# ----------------------------
features = ["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(df[features].corr(), cmap="coolwarm", vmin=-1, vmax=1)

ax.set_xticks(range(len(features)), features, rotation=45, ha="right")
ax.set_yticks(range(len(features)), features)

fig.colorbar(im, ax=ax, label="Pearson r")
ax.set_title("Sensor & Yield Correlations")

plt.tight_layout()
plt.savefig("reports/figures/corr_heatmap.png", dpi=150)
plt.close()

# ----------------------------
# 4. SCATTER PLOTS
# ----------------------------
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].scatter(df["humidity_pct"], df["yield_kg"], alpha=0.5, s=15)
axes[0].set(xlabel="Humidity (%)", ylabel="Yield (kg)")

axes[1].scatter(df["temperature_c"], df["yield_kg"], alpha=0.5, s=15)
axes[1].set(xlabel="Temperature (°C)", ylabel="Yield (kg)")

axes[2].scatter(df["co2_ppm"], df["yield_kg"], alpha=0.5, s=15)
axes[2].set(xlabel="CO₂ (ppm)", ylabel="Yield (kg)")

plt.tight_layout()
plt.savefig("reports/figures/scatter_yield.png", dpi=150)
plt.close()

print("EDA + Data Quality report completed successfully")