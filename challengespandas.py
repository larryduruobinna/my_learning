import pandas as pd
data = {"substation_id": ["S1", "S2", "S3", "S4", "S5"],
        "voltage": [230, 215, 240, 200, 225],
        "current": [50, 65, 45, 80, 55],
        "temp_c": [60, 85, 55, 95, 70],
        "breaker_ok": [True, True, False, False, True]}
df = pd.DataFrame(data)
df["power"] = df["voltage"] * df["current"]
df["power_KW"] = df["power"] / 1000
df["overheating"] = df["temp_c"] > 80
print(df)
print(df[(df["power_KW"] > 15) & (df["breaker_ok"] == True)])
print(df[(df["overheating"] == True) | (df["breaker_ok"] == False)])
print(df[["substation_id", "power_KW"]])



wind_farm = {"turbine_id": ["WT1", "WT2", "WT3", "WT4", "WT5"],
             "wind_speed_mps": [12, 8, 15, 6, 18],
             "output_KW": [450, 200, 600, 90, 750],
             "vibration_alert": [False, False, True, False, True]}
df = pd.DataFrame(wind_farm)
df["capacity_factor"] = df["output_KW"] / 750
df["high_wind"] = df["wind_speed_mps"] > 10
print(df)
print(df[(df["high_wind"] == True) & (df["vibration_alert"] == False)])
print(df[(df["output_KW"] < 200) | (df["vibration_alert"] == True)])
print(df[["turbine_id", "capacity_factor"]])


smart_grid = {"feeder_id": ["F1", "F2", "F3", "F4", "F5", "F6"],
              "voltage_V": [230, 208, 240, 195, 225, 212],
              "current_A": [120, 85, 150, 200, 95, 110],
              "frequency_Hz": [50.0, 49.8, 50.1, 48.5, 50.0, 49.9],
              "protection_relay_ok": [True, True, False, False, True, False]}
df = pd.DataFrame(smart_grid)
df["power_apparent"] = df["voltage_V"] * df["current_A"]
df["power_KVA"] = df["power_apparent"] / 1000
df["under_frequency"] = df["frequency_Hz"] < 49.5
df["fault_risk"] = (df["under_frequency"] == True) | (df["protection_relay_ok"] == False)
print(df)
print(f"Fedders with fault risk: {df["fault_risk"] == True}")
print(f"{df[(df["power_KVA"] > 20) & (df["protection_relay_ok"] == True)]}")
print(f"{df["feeder_id"], df["fault_risk"], df["power_KVA"]}")


portfolio = {"site_id": ["RE1", "RE2", "RE3", "RE4", "RE5", "RE6", "RE7"],
             "site_type": ["solar", "wind", "hydro", "solar", "wind", "hydro", "solar"],
             "capacity_MW": [50, 120, 80, 45, 150, 100, 60],
             "generation_MW": [35, 95, 78, 28, 110, 95, 42],
             "maintenance_due": [False, True, False, True, False, True, True],
             "grid_connection_ok": [True, True, False, True, False, True, True]}
df = pd.DataFrame(portfolio)
df["capacity_factor"] = df["generation_MW"] / df["capacity_MW"] 
df["efficiency_percent"] = df["capacity_factor"] * 100
df["needs_attention"] = (df["maintenance_due"] == True) | (df["grid_connection_ok"] == False)
df["high_performer"] = (df["efficiency_percent"] > 75) & (df["needs_attention"] == False)
print(df)
print(f"Urgent maintenance: {df["needs_attention"] == True}")
print(f"Best performer: {df["high_performer"] == True}")
print(f"{df["site_id"], df["efficiency_percent"], df["high_performer"]}")


water_system = {"unit_id": ["WT1", "WT2", "WT3", "WT4", "WT5", "WT6", "WT7", "WT8"],
                "flow_rate_m3h": [150, 200, 120, 180, 95, 220, 110, 175],
                "chlorine_ppm": [0.8, 1.2, 0.5, 1.5, 0.9, 1.3, 0.6, 1.1],
                "turbidity_ntu": [0.3, 0.2, 0.8, 0.1, 0.6, 0.15, 1.2, 0.25],
                "filter_clean": [True, True, False, True, False, True, False, True]}
df = pd.DataFrame(water_system)
df["daily_output_m3"] = df["flow_rate_m3h"] * 24
df["chlorine_adequate"] = df["chlorine_ppm"] >= 0.7
df["turbidity_high"] = df["turbidity_ntu"] > 0.5
df["needs_service"] = (df["filter_clean"] == False) | (df["turbidity_high"] == True)
print(df)
print(f"Requires maintenance! {df["needs_service"]}")
print("High capacity, safe units!", (df["daily_output_m3"] > 3000) & (df["chlorine_adequate"] == True))
print(f"{df["unit_id"], df["daily_output_m3"], df["needs_service"]}")


data_set = {"plant": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
        "fuel_type": ["solar", "gas", "solar", "wind", "gas", "wind", "solar", "gas"],
        "output_mw": [120, 480, 95, 210, 520, 185, 140, 455],
        "efficiency": [0.21, 0.58, 0.19, 0.42, 0.61, 0.39, 0.22, 0.55]}
df = pd.DataFrame(data_set)
report = df.groupby("fuel_type").agg({"efficiency": "mean", "output_mw": "sum"})
print(f"Dataframe: {df}")
print(f"Groupby: {report}")
report.to_csv("fuel_report.csv")
df = pd.read_csv("fuel_report.csv")
print(df)


data_farm = {"turbine": ["WT1", "WT2", "WT3", "WT4", "WT5", "WT6", "WT7", "WT8", "WT9"],
             "site": ["coastal", "inland", "coastal", "mountain", "inland", "coastal", "mountain", "inland", "mountain"],
             "energy_mwh": [3200, 2100, 3450, 2800, 1950, 3300, 2650, 2250, 2900],
             "availability": [0.97, 0.89, 0.95, 0.92, 0.85, 0.96, 0.91, 0.88, 0.93]}
df = pd.DataFrame(data_farm)
report = df.groupby("site").agg({"energy_mwh": "sum", "availability": "mean"})
print(df)
print(f"Groupby site: {report}")
report.to_csv("site_report.csv")
report_file = pd.read_csv("site_report.csv")
print(f"Report_file: {report_file}")
print(f"Original dataset: {df}")
