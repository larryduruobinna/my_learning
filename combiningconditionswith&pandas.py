import pandas as pd
# IN PANDAS YOU CAN NOT PLAIN PYTHON "AND". YOU MUST USE & INSTEAD AND WRAP EACH CONDITIONS IN PARENTHESIS.
# EXAMPLE:

data = {"temp_c": [ 70, 90, 85],
        "load_percent": [100, 55, 75],
        "voltage": [240, 230, 210],
        "status": [True, False, True]}
df = pd.DataFrame(data)
print(df)
print(df[df["temp_c"] > 80])
print(df[(df["temp_c"] > 80) & (df["load_percent"] > 60)])
print(df[(df["status"] == True) & (df["temp_c"] > 50)])



# FOR "OR" USE |
print(df[(df["temp_c"] > 80) | (df["status"] == False)])


# CHALLENGE:

data_tr = {"transformer_id": ["T1", "T2", "T3"],
           "temp_c": [68, 95, 72],
           "load_percent": [55, 92, 60],
           "oil_level_ok": [True, True, False]}
df = pd.DataFrame(data_tr)
print(df)
print(df[(df["temp_c"] > 80) & (df["load_percent"] > 60)])
print(df[(df["temp_c"] > 80) | (df["oil_level_ok"] == False)])

# CHALLENGE2:


data_cb = {"breaker_id": ["B1", "B2", "B3", "B4"],
        "current_A": [80, 150, 60, 200],
        "age_years": [5, 12, 2, 15],
        "tripped": [False, True, False, True]}
df = pd.DataFrame(data_cb)
print(df)
print(df[(df["current_A"] > 100) & (df["age_years"] > 10)])
print(df[(df["current_A"] > 100) | (df["tripped"] == True)])

# CHALLENGE3:
data_solar = {"panel_id": ["P1", "P2", "P3", "P4", "P5"],
              "output_watts": [280, 150, 300, 90, 275],
              "temp_c": [45, 60, 42, 65, 47],
              "shaded": [False, True, False, True, False]}
df = pd.DataFrame(data_solar)
print(df)
print(df[(df["output_watts"] < 200) & (df["shaded"] == True)])
print(df[(df["temp_c"] > 50) | (df["output_watts"] < 100)])