import csv
import json
import sys
from pathlib import Path

# Allow very large CSV fields (safe limit for Windows)
csv.field_size_limit(10_000_000)

# 1. Define file paths
input_csv = Path("data/data raw/enterprise_data.csv")
output_json = Path("data/data processed/enterprise_data.json")

# 2. Create empty list to store records
data = []

# 3. Open and read CSV file
with open(input_csv, mode="r", encoding="utf-8", errors="ignore") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        data.append(row)

# 4. Write data to JSON file
with open(output_json, mode="w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

# 5. Confirmation message
print("CSV successfully converted to JSON!")
print("Total records:", len(data))
