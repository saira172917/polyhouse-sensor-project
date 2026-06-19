| Scenario           | Temperature (°C) | Humidity (%) | CO₂ (ppm) | Expected Behaviour                  |
| ------------------ | ---------------- | ------------ | --------- | ----------------------------------- |
| Optimal conditions | 22               | 88           | 900       | Normal yield prediction             |
| Dry spell          | 28               | 55           | 900       | Lower yield than optimal            |
| Heat spike         | 35               | 80           | 900       | Yield changes noticeably            |
| High humidity      | 22               | 98           | 900       | Yield changes; warning may appear   |
| Extreme CO₂        | 22               | 88           | 1800      | Prediction works; CO₂ warning shown |



| Scenario      | CLI Output | Streamlit Output | Match |
| ------------- | ---------- | ---------------- | ----- |
| Optimal       | 16.84 kg   | 16.84 kg         | ✅     |
| Dry spell     | 15.21 kg   | 15.21 kg         | ✅     |
| Heat spike    | 14.76 kg   | 14.76 kg         | ✅     |
| High humidity | 17.03 kg   | 17.03 kg         | ✅     |
| Extreme CO₂   | 16.59 kg   | 16.59 kg         | ✅     |
