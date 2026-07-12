import pandas as pd
# READING A FILE 
df = pd.read_csv("data.csv")
print(df)  # THIS READS A FILE AND TURNS IT INTO A DATAFRAME

# WRITING TO A FILE:
# AFTER CLEANING OR CHANGING YOUR DATA YOU SAVE IT
df.to_csv("cleaned_file.csv")
# EXAMPLE:
# READ THE FILE
df = pd.read_csv("data.csv")
print(df)
# SAVE IT
df.to_csv("output1.csv", index=False)
print("Saved!")


df = pd.read_csv("solar_farm.csv")
filled = df.fillna(df[["generation_KWh", "efficiency_percent"]].mean(numeric_only=True))
df["high_performer"] = df["efficiency_percent"] > 93
df["Normal"] = df["efficiency_percent"] <= 93
needs_maintenance = df["maintenance_due"] = True
print("\nDataFrame for solar_farm:")
print(df)
print("\nSum of missing values per column:")
print(df.isna().sum())
print("\nFill missing values with mean:")
print(filled)
print("\nNeeds maintenance:")
print(needs_maintenance)
df.to_csv("solar_farm_report.csv", index=False)
print("\nReport saved to solar_farm_report.csv")




df = pd.read_csv("turbines.csv")
df["efficiency"] = df["output_KW"] / 750
print(df)
filtered = df[df["vibration_alert"] == True]
print(filtered)
filtered.to_csv("turbines.csv", index=False)
print("Saved!")


df = pd.read_csv("power_plants.csv")
print(df)
filtered = df[df["fuel_type"] == "coal"]
filtered.to_csv("power_plants.csv", index=False)
print("Saved")


df = pd.read_csv("grid_voltage.csv")
print(df)
filtered = df[df["status"] == "Active"]
filtered.to_csv("active_grid.csv")
print("Done!")


df = pd.read_csv("plants.csv")
print(df)
filtered = df[df["fuel_type"] == "Coal"]
filtered.to_csv("coal_plants.csv", index=False)