# FILE HANDLING MEANS READING AND WRITING DATA TO A FILE.
# IN REAL INDUSTRIAL SYSTEMS, SENSOR DATA IS SAVED TO FILES. YOU READ IT ALTER FOR ANALYSIS.
# FOR EXAMPLES:
# WRTINF TO A FILE:  w(means write, creates file, overwrite if exists), \n(means new line), Always close() the file when done
file = open("readings.txt","w")
file.write("voltage: 230V\n")
file.write("current: 15A\n")
file.write("status: NORMAL\n")
file.write("no of turns: 5\n")
file.close()

# READING FROM A FILE:
file = open("readings.txt", "r")
content = file.read()
file.close()
print(content)


with open("readings.txt", "w") as file:
    file.write("voltage: 230V\n")
    file.write("current: 15A\n")
with open("readings.txt", "r") as file:
    content = file.read()
    print(content)


with open("readings.txt", "w") as file:
    file.write("Name: Larry\n")
    file.write("Age: 24\n")
    file.write("Occupation: Engineer\n")
with open("readings.txt", "r") as file:
    content = file.read()
    print(content)

# APPENDING: ADD TO EXISTING FILE
with open("readings.txt", "a") as file:
    file.write("Frequency: 50Hz\n")
with open("readings.txt", "r") as file:
    content = file.read()
    print(content)



#CHALLENGE
with open("sensor_log.txt", "w") as file:
    file.write("Sensor!: 75\n")
    file.write("Sensor2: 63\n")
    file.write("sensor3: 82\n")
with open("sensor_log.txt", "r") as file:
    content = file.read()
    print(content)


with open("larrys_log.txt", "w") as file:
    file.write("Name: Larryduru Emmanuel\n")
    file.write("Age: 25 years old\n")
    file.write("Occupation: Machine Learning Engineer\n")
with open("larrys_log.txt", "r") as file:
    content = file.read()
    print(content)


with open("dectrons_log.txt", "w") as file:
    file.write("CEO: Stephane\n")
    file.write("HR: Carla\n")
    file.write("Plant Manager: kane\n")
with open("dectrons_log.txt", "r") as file:
    content = file.read()
    print(content)


with open("investment_log.txt", "w") as file:
    file.write("Company1: Oil and Gas\n")
    file.write("Company2: leoj Engineering\n")
    file.write("Company3: AI Academy for Engineering\n")
with open("investment_log.txt", "r") as file:
    content = file.read()
    print(content)