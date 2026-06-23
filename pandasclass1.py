import pandas as pd

current = pd.Series([4.5, 4.7, 5.2, 4.9])
print(current)

data = {"time": ["8:00", "9:00", "10:00"],
        "voltage": [11.2, 10.8, 9.1],
        "current": [4.5, 4.7, 5.2],
        "status": ["OK", "OK", "FAULT"]}
df = pd.DataFrame(data)
print(df)

# CHALLENGE1:
data2 = {"hour": [1, 2, 3],
        "temp_c": [45, 48, 52],
        "load_percent": [60, 65, 80]}
df = pd.DataFrame(data2)
print(df)
data3 = {"relay_id": ["R1", "R2", "R3", "R4"],
        "trip_current_A": [100, 120, 95, 110],
        "response_time_ms": [15, 18, 12, 20],
        "tripped": [True, False, False, True]}
df = pd.DataFrame(data3)
print(df)
print(df["trip_current_A"])
print(df[["tripped", "response_time_ms"]])
print(df[df["trip_current_A"] > 100])
print(df[df["response_time_ms"] > 15])


data_tr = {"transformer_id": ["T1", "T2", "T3"],
           "temp_c": [68, 95, 72],
           "load_percent": [55, 92, 60],
           "oil_level_ok": [True, True, False]}
df = pd.DataFrame(data_tr)
print(df[df["temp_c"] > 80])
print(df[df["oil_level_ok"] == False])