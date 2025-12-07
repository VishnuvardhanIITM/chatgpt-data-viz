import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("employee_data.csv")

# Calculate HR count
hr_count = data[data["Department"] == "HR"].shape[0]
print("HR Count:", hr_count)

# Create department distribution histogram (bar chart)
plt.figure(figsize=(6, 4))
data["Department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.tight_layout()

# Save the plot as an image
plt.savefig("histogram.png")
plt.close()
