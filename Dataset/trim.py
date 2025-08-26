import pandas as pd
import os

# Define input and output paths
input_path = r"C:\Users\iakbaral\Downloads\archive (1)\Retail_Transactions_Dataset.csv"
output_dir = r"C:\Users\iakbaral\Downloads\RetailDemandForecast\Dataset"
output_path = os.path.join(output_dir, "Retail_Transactions_Dataset.csv")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read the CSV and take the first 100,000 rows
df = pd.read_csv(input_path)
df_subset = df.head(30000)

# Save the subset to the output path
df_subset.to_csv(output_path, index=False)

print(f"Saved first 30,000 rows to: {output_path}")
