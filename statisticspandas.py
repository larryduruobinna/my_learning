import pandas as pd


df = pd.read_csv("volts.csv")
print(df)
mean = df["voltage_V"].mean()
max = df["voltage_V"].max()
min = df["voltage_V"].min()
stats = df["voltage_V"].describe()
print(f"Mean voltages: {mean}")
print(f"Max voltage: {max}")
print(f"Min voltage: {min}")
print(f"Stats of voltage: {stats}")