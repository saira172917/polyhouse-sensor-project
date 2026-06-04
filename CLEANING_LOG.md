\# Cleaning Log – Polyhouse Sensor Dataset



\## Dataset Overview

Polyhouse sensor dataset used for yield prediction with environmental parameters.



---



\## Null Counts Before Cleaning



temperature\_c: 5  

humidity\_pct: 5  

soil\_moisture\_pct: 5  

light\_lux: 5  

co2\_ppm: 5  



---



\## Null Counts After Cleaning



All columns: 0 null values



---



\## Imputation Strategy (Agritech Reasoning)



\- temperature\_c → median (stable environmental variation)

\- humidity\_pct → median (normal greenhouse fluctuations)

\- soil\_moisture\_pct → forward fill (gradual soil changes)

\- light\_lux → median (sensor noise handling)

\- co2\_ppm → median (controlled greenhouse environment)



---



\## Summary

All missing values were successfully handled and dataset is now clean and ready for machine learning.

