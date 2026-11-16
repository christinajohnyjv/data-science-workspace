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
print(df)

max_eye_pressure=df['eye_pressure'].max()
min_eye_pressure=df['eye_pressure'].min()
print(max_eye_pressure)
print(min_eye_pressure)

count=df['diagnosis'].value_counts()
print(count)

# Filter and print only the rows where diagnosis == "Glaucoma"
gla= df[df["diagnosis"] == "Glaucoma"]
print(gla)

high_risk = df[(df["eye_pressure"] > 20.0) & (df["is_smoker"] == True)]
print(high_risk)

# average age of only the Glaucoma patients
glaucoma_avg_age=gla['age'].mean()
print(round(glaucoma_avg_age,2))