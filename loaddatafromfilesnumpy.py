import numpy as np
#  IN REAL AI AND ML WORK DATA DOES NOT COME AS NUMBERS YOU TYPE MANUALLY. THEY COME FROM FILES. YOUR SENSOR LOGS. YOUR SUBSTATION RECORDS. YOUR MOTOR DATA. NUMPY CAN SAVE AND LOAD THAT DATA IN ONE LINE EACH.
#  WHAT ARE CVS FILES:  THEY MEAN COMMA SEPERATED VALUES. ITS JUST A TEXT FILE IWTH NUMBERS SEPERATED BY COMMAS. EXAMPLE:
220,230,215,240,228

# HOW TO SAVE DATA TO A FILE:
voltages = np.array([220, 230, 215, 240, 228])
np.savetxt("voltages.csv", voltages, delimiter=",")
print("File saved!")

# HOW TO LOAD DATA FROM FILE:
loaded = np.loadtxt("voltages.csv", delimiter=",")
print("Loaded data:", loaded)
# delimeter means the values are seperated by commas.

#  FULL EXAMPLE -- 1D ARRAY:
currents = np.array([15, 8, 5, 11, 10])
np.savetxt("current.csv", currents, delimiter=",")
print("File saved!")
load_currents = np.loadtxt("current.csv", delimiter=",")
print("Load currents:", load_currents)


# FULL EAXMPLE -- 2D ARRAY:
substation = np.array([[220, 225, 230, 228], [210, 215, 212, 218], [240, 238, 235, 242]])
np.savetxt("substation.csv", substation, delimiter=",")
print("File saved!")
load_substation = np.loadtxt("substation.csv", delimiter=",")
print("Load substation:", load_substation)

sensors = np.array([[2, 4, 5, 3, 1], [10, 11, 17, 2, 13], [15, 9, 7, 22, 18]])
np.savetxt("sensors.csv", sensors, delimiter=",")
print("File saved!")
load_sensors = np.loadtxt("sensors.csv", delimiter=",")
print("Loaded sensor data:", load_sensors)


# CHALLENGE:
motors = np.array([[5, 8, 12, 20, 35], [6, 9, 14, 22, 38], [4, 7, 10, 18, 30]])
np.savetxt("motors.csv", motors, delimiter=",")
print("File saved!")
load_motors = np.loadtxt("motors.csv", delimiter=",")
print("Load motors data:", load_motors)
print("Max current per motor:", np.max(motors, axis=1))