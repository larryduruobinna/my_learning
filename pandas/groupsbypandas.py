import pandas as pd
df = pd.read_csv("power_plant1.csv")
print(df)
group = df.groupby("fuel_type")["efficiency_percent"].mean()
print(f"Grouped by fuel type efficiency mean: {group}")
group1 = df.groupby("fuel_type")["capacity_MW"].sum()
print(f"Grouped by fuel type capacity sum: {group1}")
group2 = df.groupby("fuel_type")["plant_id"].size()
print(f"Grouped by fuel type count of plant: {group2}")


df = pd.read_csv("renewable.csv")
print(df)
grouped1 = df.groupby("energy_source")["efficiency_percent"].mean()
grouped2 = df.groupby("energy_source")["power_output_MW"].sum()
grouped3 = df.groupby("energy_source").size()
print(f"Grouped by energy source mean efficiency: {grouped1}")
print(f"Grouped by energy source sum power output: {grouped2}")
print(f"Grouped by energy source counts for facility: {grouped3}")