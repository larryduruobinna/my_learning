import numpy as np
import pandas as pd
voltages = np.array([3.7, 2.8, 3.6, 2.9, 3.8, 3.1, 2.7, 3.5])
low_cells = voltages < 3
print(f"Sum of cells below 3.0V:{np.sum(low_cells)}")
print(f"voltages of those weak cells:{voltages[low_cells]}")
print(f"Average voltages of the whole pack:{np.mean(voltages)}")
print(f"Highest voltage:{np.max(voltages)}")
print(f"Lowest voltages:{np.min(voltages)}")

df = pd.read_csv("challenge1.csv")
weekday_average = df[df["day"].isin(["mon", "tue", "wed", "thu", "fri"])]["consumption"].mean()
print(f"Average consumption across all days:{df["consumption"].mean()}")
print(f"Highest consumption value:{df["consumption"].max()}")
print(f"Rows with temperture below 20:{df[df["temperature"] < 20]}")
print(f"Average weekday consumption:{weekday_average}")


data = {"transformer": ["T1", "T2", "T3", "T4", "T5", "T6"],
        "rated_kva": [500, 1000, 750, 500, 1500, 1000],
        "load_kva": [420, 890, 710, 260, 1380, 950]}
df = pd.DataFrame(data)
df["load_percent"] = df["load_kva"] / df["rated_kva"] * 100
needs_maintenance = df[df["load_percent"] > 85]
print(df)
print(f"Needs maintenance:{needs_maintenance}")

data_sub = {"substation": ["S1", "S2", "S3", "S4", "S5", "S6","S7"],
        "voltage": [228, 241, 219, 235, 246, 230, 224],
        "region": ["North", "South", "North", "East", "South", "East", "North"]}
df = pd.DataFrame(data_sub)
needs_attention = df[(df["voltage"] < 225) | (df["voltage"] > 245)]
sort = df.sort_values(by="voltage", ascending=False)
print(f"Needs attention:{needs_attention}")
print(f"Voltage descending:{sort}")

data_gen = {"generator": ["G1", "G2", "G3", "G4", "G5"],
            "output": [45.2, np.nan, 38.7, 51.0, np.nan],
            "fuel_type": ["gas", "hydro", "gas", "coal", "hydro"]}
df = pd.DataFrame(data_gen)
missing_values = df.isna().sum()
fill = df.fillna(df.mean(numeric_only=True))
cleaned = fill["output"].describe()
print(df)
print(missing_values)
print(fill)
print(cleaned)

data_region = {"plant": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
               "fuel_type": ["solar", "gas", "solar", "wind", "gas", "wind", "solar", "gas"],
               "output_mw": [120, 480, 95, 210, 520, 185, 140, 455],
               "efficiency": [0.21, 0.58, 0.19, 0.42, 0.61, 0.39, 0.22, 0.55]}

df = pd.DataFrame(data_gen)
group = df.groupby("fuel_type")["efficiency"].mean()
