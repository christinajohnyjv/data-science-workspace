import pandas as pd

clinical_records = {
    "patient_id": ["D01", "D02", "D03", "D04", "D05", "D06", "D07"],
    "age": [45, 60, 38, 72, 55, 65, 40],
    "glucose_level": [95, 180, 105, 210, 145, 195, 110],
    "stage": ["Normal", "Type-2", "Normal", "Type-2", "Pre-diabetes", "Type-2", "Normal"],
    "on_medication": [False, True, False, True, False, True, False]
}

df=pd.DataFrame(clinical_records)
print(df.shape)

# Count Occurrences of Each Stage
print(df['stage'].value_counts())

# Filter Only 'Type-2' Patients
diabetes=df[df["stage"]=="Type-2"]
print(diabetes)

# Add high_glucose column
df["high_glucose"] = df["glucose_level"] > 140
print(df)

# GroupBy stage and get average glucose
print(df.groupby("stage")["glucose_level"].mean())

# Filter Type-2 AND Age >= 65
high_risk = df[(df["stage"] == "Type-2") & (df["age"] >= 65)]
print(high_risk)