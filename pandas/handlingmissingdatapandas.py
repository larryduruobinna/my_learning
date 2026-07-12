import pandas as pd
import numpy as np


data = {"turbine_id": ["T1", "T2", "T3", "T4", "T5"],
        "output_KW": [450, np.nan, 600, np.nan, 750],
        "temperature_C": [35, 40, np.nan, 45, 50]}
df = pd.DataFrame(data)
dropped = df.dropna()
fill = df.fillna(df.mean(numeric_only=True))
print(df)
print(df.isna())
print(df.isna().sum())
print(dropped)
print(fill)

power_grid = {"substation_id": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"],
              "voltage_V": [230, np.nan, 240, 195, 225, np.nan, 235, 220],
              "current_A": [50, 65, np.nan, 80, 55, 60, np.nan, 70],
              "frequency_Hz": [50.0, 49.8, 50.1, np.nan, 50.0, 49.9, 50.2, np.nan]}
df = pd.DataFrame(power_grid)
dropped_missing = df.dropna()
filled_missing = df.fillna(df.mean(numeric_only=True))
print("==POWER GRID DATA==")
print(f"DataFrame Power Grid:{df}")
print(f"Missing data:{df.isna()}")
print(f"Count of missing values:{df.isna().sum()}")
print(f"Dropped missing values from power grid:{dropped_missing}")
print(f"Missing values from power grid filled with mean of column:{filled_missing}")



water_plant = {"unit_id": ["U1", "U2", "U3", "U4", "U5", "U6"],
               "flow_rate": [150, np.nan, 120, 180, np.nan, 220],
               "ph_level": [7.0, 7.2, np.nan, 7.1, 6.9, np.nan],
               "turbidity": [0.3, 0.2, 0.8, np.nan, 0.6, 0.15]}
df = pd.DataFrame(water_plant)
dropped = df.dropna()
filled = df.fillna(df.mean(numeric_only=True))
print("== DATA FOR WATER TREATMENT PLANT==")
print(f"Data frame for water plant:{df}")
print(f"Total missing values for each column:{df.isna().sum()}")
print(f"Total missing values from flow_rate column:{df["flow_rate"].isna().sum()}")
print(f"Dropped columns with missing values:{dropped}")
print(f"Filled missing values with mean of column:{filled}")