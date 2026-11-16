import pandas as pd

patients = {
    "patient_id": ["P101", "P102", "P103", "P104", "P105", "P106"],
    "age": [52, 67, 41, 75, 60, 48],
    "eye_pressure": [14.2, 22.5, 15.0, 26.1, 19.8, 16.5],
    "diagnosis": ["Healthy", "Glaucoma", "Healthy", "Glaucoma", "Glaucoma", "Healthy"],
    "is_smoker": [False, True, False, True, False, True]
}
# Creating Dataframe
df=pd.DataFrame(patients)
print('\n',df)
# Highest and lowest value of eye_pressure
max_eye_pressure=df['eye_pressure'].max()
min_eye_pressure=df['eye_pressure'].min()
print("\nThe highest eye_pressure:", max_eye_pressure)
print("The lowest value eye_pressure:", min_eye_pressure)
# Category Count
count=df['diagnosis'].value_counts()
print("\nDiagnosis Count\n", count)
# Row Filtering: where diagnosis == "Glaucoma"
glaucoma_patient= df[df["diagnosis"] == "Glaucoma"]
print("\nThe Glaucoma Patients Only\n", glaucoma_patient)
# High-Risk Filter (Two Conditions)
high_risk = df[(df["eye_pressure"] > 20.0) & (df["is_smoker"] == True)]
print("\nHigh Risk Patients (Pressure > 20 & Smoker)\n", high_risk)
# Average age of only the Glaucoma patients
glaucoma_avg_age=glaucoma_patient['age'].mean()
print("\nThe average age of Glaucoma patients:", round(glaucoma_avg_age,2))