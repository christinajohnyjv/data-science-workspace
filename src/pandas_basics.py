import pandas as pd
clinical_data = {
    "patient_id": ["P001", "P002", "P003", "P004", "P005"],
    "age": [45, 62, 35, 71, 58],
    "condition": ["Normal", "AMD", "DME", "AMD", "Normal"],
    "retinal_thickness": [95.5, 142.0, 160.2, 138.5, 92.0],
    "has_diabetes": [False, True, True, False, False]
}
# Convert into a Pandas DataFrame
df=pd.DataFrame(clinical_data)
print(df)
print(df.shape)
print(df.head(3))
# find age's average
avg_age=df['age'].mean()
print("The average age is ",avg_age)
# Count occurrences of each condition 
count=df['condition'].value_counts()
print("The occurrences of each condition:", count)
# summary of all numeric columns
print(df.describe())