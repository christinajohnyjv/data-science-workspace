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

df["high_sugar"] = df["blood_sugar"] >= 180
print(df)

fil=df[(df["category"]=="DME") & (df["high_sugar"]==True)]
print(fil)

disease_type=df.groupby("category")["retinal_thickness"].mean()
print(round(disease_type,1))

def get_column_metrics(df, column_name):
    min_val=np.min(column_name)
    max_val=np.max(column_name)
    avg_val=np.mean(column_name)
    return min_val, max_val, avg_val 

arr = np.array(df["retinal_thickness"])
print(get_column_metrics(df,arr))    