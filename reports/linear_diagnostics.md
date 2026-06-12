# Linear Regression Diagnostics Report

## 📊 Objective
To analyze residual behavior of the Linear Regression model and evaluate whether it is suitable as a baseline for polyhouse yield prediction.

---

## 📉 Residual Analysis (Key Findings)

### 1. Residuals vs Predicted Yield
- Residuals are mostly centered around zero.
- However, slight patterning appears at higher predicted values.
- This suggests the model may struggle with extreme yield predictions.

### 2. Residuals vs Humidity
- Weak but visible structure in residual distribution.
- Indicates humidity may have a non-linear relationship with yield.
- Linear model may not fully capture this interaction.

---

## ⚠️ Model Limitations
- Linear Regression assumes linear relationships between features and target.
- Environmental factors (temperature, humidity, CO₂) likely interact non-linearly.
- Model shows signs of heteroscedasticity (changing error variance).

---

## 📌 Key Insight
Residuals are not completely random, indicating missing complexity in the model.

This suggests that:
- Important feature interactions may be missing
- Non-linear relationships exist in the dataset

---
## 📌 Coefficient Interpretation (Linear Model)

The Linear Regression coefficients represent how each environmental factor influences crop yield:

- Temperature: affects yield within an optimal range; extreme values may reduce productivity.
- Humidity: generally shows a positive relationship with yield, supporting plant growth conditions.
- CO₂ concentration: contributes positively to yield due to enhanced photosynthesis.

Overall, the coefficients confirm that environmental conditions have measurable but partially linear effects on crop yield.

## 📈 Conclusion

Linear Regression is a **good baseline model**, but not sufficient for final prediction.

---

## 🚀 Recommendation

- Proceed with **Random Forest Regressor** or other non-linear models
- Add feature interactions or lag-based features
- Evaluate improvement over this baseline

---

## 🧠 Final Verdict

✔ Good interpretability  
❌ Limited predictive power  
➡ Use as baseline only, not production model
The Linear Regression model achieved an R² score of 0.427, indicating that it explains approximately 42.7% of the variability in crop yield. This is acceptable as a baseline model and provides a useful benchmark for comparison with more advanced non-linear models, which may better capture complex interactions among environmental factors.