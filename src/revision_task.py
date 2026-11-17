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
print(df['stage'].value_counts())