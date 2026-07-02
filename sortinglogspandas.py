import pandas as pd
data_1 = {"voltage": [230, 208, 240, 195, 225],
          "current": [50, 65, 45, 80, 55]}
df = pd.DataFrame(data_1)
sorted_data = df.sort_values(by="voltage")
sorted_data2 = df.sort_values(by="voltage", ascending=False)
print(df)
print(sorted_data)
print(sorted_data2)

#CHALLENGE:
data_2 = {"turbine_id": ["T1", "T2", "T3", "T4"],
          "output_KW": [450, 200, 600, 90]}
df = pd.DataFrame(data_2)
sorted_df = df.sort_values(by="output_KW", ascending=False)
sorted_df2 = df.sort_values(by="turbine_id")
print(df)
print(sorted_df)
print(sorted_df2)




data = {"plant_id": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
        "fuel_type": ["Coal", "Gas", "Coal", "Gas", "Nuclear", "Coal", "Gas", "Nuclear"],
        "capacity_MW": [500, 350, 600, 400, 800, 450, 380, 750],
        "output_MW": [380, 310, 480, 360, 760, 360, 320, 710],
        "maintenance_cost_M": [2.5, 1.2, 3.1, 1.8, 4.2, 2.8, 1.5, 3.9]}
df = pd.DataFrame(data)
df["efficiency"] = df["output_MW"] / df["capacity_MW"]
df["efficiency_percent"] = df["efficiency"] * 100
sort_data = df.sort_values(by="efficiency_percent", ascending=False)
sort_data2 = df.sort_values(by="maintenance_cost_M")
sort_data3 = df.sort_values(by="plant_id")
print(df)
print(sort_data2[["plant_id", "maintenance_cost_M"]])
print(sort_data3)


data_4 = {"unit_id": ["U1", "U2", "U3", "U4", "U5", "U6"],
        "flow_rate_m3h": [150, 200, 120, 180, 95, 220],
        "chlorine_ppm": [0.8, 1.2, 0.5, 1.5, 0.9, 1.3],
        "turbidity_ntu": [0.3, 0.2, 0.8, 0.1, 0.6, 0.15],
        "filter_age_years": [2, 1, 4, 3, 5, 2]}
df = pd.DataFrame(data_4)
df["daily_output_m3"] = df["flow_rate_m3h"] * 24
df["efficiency"] = df["daily_output_m3"] / 5000
df["needs_filter_replacement"] = df["filter_age_years"] > 3
sort_filter_age = df.sort_values(by=["filter_age_years", "unit_id"], ascending=[True, True])
sort_efficiency = df.sort_values(by="efficiency", ascending=False)
sort_needs_replacement = df.sort_values(by=["needs_filter_replacement", "efficiency"], ascending=[True, False])
print(df)
print(sort_filter_age[["unit_id", "filter_age_years"]])
print(sort_efficiency)
print(sort_needs_replacement)
