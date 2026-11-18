import numpy as np
import pandas as pd

screening_data = {
    "patient_id": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "blood_sugar": [110, 185, 95, 220, 140, 260],
    "retinal_thickness": [95.0, 155.0, 90.0, 175.0, 120.0, 190.0],
    "category": ["Normal", "DME", "Normal", "DME", "Normal", "DME"]
}

# Create the DataFrame
df=pd.DataFrame(screening_data)
print(df)

# Add Risk Column
df["high_sugar"] = df["blood_sugar"] >= 180
print(df)

# Filter High-Risk DME Cases
critical_cases=df[(df["category"]=="DME") & (df["high_sugar"]==True)]
print(critical_cases)

# GroupBy and Average Retinal Thickness
disease_type=df.groupby("category")["retinal_thickness"].mean()
print(round(disease_type,1))

# Reusable NumPy Analysis Function
def get_column_metrics(df, column_name):
    arr = np.array(df[column_name]) 
    min_val=np.min(arr)
    max_val=np.max(arr)
    avg_val=np.mean(arr.round(1))
    return min_val, max_val, avg_val 

min_t, max_t, mean_t = get_column_metrics(df, "retinal_thickness")
print(f"Retinal Thickness -> Min: {min_t} μm | Max: {max_t} μm | Mean: {mean_t} μm")