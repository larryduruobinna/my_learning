import pandas as pd
data = {"voltage": [220, 210, 225],
        "current": [10, 12, 9]}
df = pd.DataFrame(data)
df["power"] = df["voltage"] * df["current"]
print(df)
df["power_KW"] = df["power"] / 1000
print(df)


data_gen = {"generator_id": ["G1", "G2", "G3", "G4"],
            "voltage": [230, 225, 240, 235],
            "current": [15, 20, 18, 12],
            "fuel_percent": [80, 45, 90, 30]}
df = pd.DataFrame(data_gen)
print(df)
df["power"] = df["voltage"] * df["current"]
print(df)
df["power_KW"] = df["power"] / 1000
print(df)
df["low_fuel"] = df["fuel_percent"] < 50
print(df)