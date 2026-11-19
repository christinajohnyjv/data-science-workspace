import matplotlib.pyplot as plt
import pandas as pd

clinical_records = {
    "condition": ["Normal", "AMD", "DME", "Normal", "AMD", "DME", "AMD", "Normal"],
    "retinal_thickness": [95.0, 145.0, 165.0, 92.0, 138.0, 172.0, 150.0, 98.0]
}

df = pd.DataFrame(clinical_records)

# Create a Bar Chart of Disease Counts
counts = df["condition"].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(counts.index, counts.values, color=["skyblue", "salmon", "lightgreen"])
plt.title("Distribution of Retinal Conditions")
plt.xlabel("Diagnosis Category")
plt.ylabel("Number of Patients")