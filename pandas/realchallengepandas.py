import pandas as pd

df = pd.read_csv("power_plant1.csv")
print(df)
df["cost_efficiency"] = df["output_MW"] / df["capacity_MW"]
coal_power = df[df["fuel_type"] == "coal"]
needs_maintenance = df[df["maintenance_due"] == True]
group_1 = df.groupby("fuel_type")["efficiency_percent"].mean()
group_2 = df.groupby("fuel_type")["capacity_MW"].sum()
group_3 = df.groupby("fuel_type").size()
mean = df["efficiency_percent"].mean()
max = df["efficiency_percent"].max()
min = df["efficiency_percent"].min()
print(coal_power)
print(needs_maintenance[["substation_id", "efficiency_percent"]])
print(group_1)
print(group_2)
print(group_3)
print(mean)
print(max)
print(min)
df.to_csv("power_grid_report.csv", index=False)



df = pd.read_csv("grid_data.csv")
print(df)
missing_values = df.isna().sum()
filled = df.fillna(df["voltage_V"].mean(numeric_only=True))
df["cost_efficiency"] = df["output_MW"] / df["capacity_MW"]
coal_plants = df[df["fuel_type"] == "coal"]
needs_maintenance = df[df["maintenance_due"] == True]
sorted_efficiency = df.sort_values(by="efficiency_percent", ascending=False)
group_1 = df.groupby("fuel_type")["efficiency_percent"].mean()
group_2 = df.groupby("fuel_type")["capacity_MW"].sum()
group_3 = df.groupby("fuel_type").size()
mean = df["efficiency_percent"].mean()
max = df["efficiency_percent"].max()
min = df["efficiency_percent"].min()
print(missing_values)
print(filled)
print(coal_plants)
print(needs_maintenance)
print(sorted_efficiency)
print(group_1)
print(group_2)
print(group_3)
print(mean)
print(max)
print(min)
df.to_csv("power_grid_final.csv")