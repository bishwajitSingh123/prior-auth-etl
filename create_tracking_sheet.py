import pandas as pd
import os

# Create tracking folder
os.makedirs("tracking", exist_ok=True)

# Define columns
columns = [
    "Procedure_ID",
    "CPT_Code",
    "Procedure_Name",
    "Tier1_Status",
    "Tier2_Status",
    "Tier3_Status",
    "Tier4_Status",
    "Tier5_Status",
    "Validation_Status",
    "Final_Status"
]

# Create dataframe
df = pd.DataFrame(columns=columns)

# Save Excel
output_path = "tracking/CPT_Master_Tracking.xlsx"

df.to_excel(output_path, index=False)

print(f"Tracking sheet created successfully at: {output_path}")