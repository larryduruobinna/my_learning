import numpy as np

substation_data = np.array([[225, 230, 228, 235, 240, 238], 
                            [210, 215, 212, 208, 214, 211], 
                            [240, 238, 242, 239, 241, 243], 
                            [220, 215, 218, 212, 216, 219]])
print("Shape:", substation_data.shape)
print("Average per substation:", np.mean(substation_data, axis=1))
print("Grid maximum:", np.max(substation_data))
print("Grid stability:", np.std(substation_data))
print("Substation2 hour3:", substation_data[1,2])
print("Substation4:", substation_data[3])
print("Peak hours2:", substation_data[:, 1:4])
print("After fault:", substation_data + 10)
print("Transformer output:", substation_data/11)
print("Reshaped:", substation_data.reshape(6, 4))

np.savetxt("substation_report.csv", substation_data, delimiter=",")
print("File saved!")

load_substation_data = np.loadtxt("substation_report.csv", delimiter=",")
print("Loaded report:", load_substation_data)
print("Max per substation:", np.max(load_substation_data, axis=1))



# CHALLENGE2:
grid = np.array([[225, 230, 228, 235, 240, 238, 222, 219], 
                 [210, 215, 212, 208, 214, 211, 209, 213], 
                 [240, 238, 242, 239, 241, 243, 237, 240], 
                 [220, 215, 218, 212, 216, 219, 214, 217], 
                 [230, 235, 233, 238, 242, 240, 236, 234]])

print("Shape:", grid.shape)
print("Average per substatiom:", np.mean(grid, axis=1))
print("Max grid:", np.max(grid))
print("Min grid:", np.min(grid))
print("Stability per substation:", np.std(grid, axis=1))
print("Substation3 hour5:", grid[2, 4])
print("Substation5:", grid[4, :])
print("Hour1 readings:", grid[:, 0])
print("Peak hours:", grid[:, 2:6])
print("Fault voltage:", grid + 8)
print("Output voltages:", grid / 11)
print("Reshaped:", grid.reshape(8, 5))
np.savetxt("grid_report.csv", grid, delimiter=",")
print("File save!")
load_grid = np.loadtxt("grid_report.csv", delimiter=",")
print("Loaded grid report:", load_grid)
print("Max per substation from loaded data:", np.max(load_grid, axis=1))



#CHALLENGE3:

smart_grid = np.array([[12, 15, 18, 20, 35, 22, 14],
                       [8, 10, 12, 15, 13, 11, 9],
                       [20, 22, 25, 28, 60, 24, 21],
                       [5, 7, 9, 11, 8, 6, 7],
                       [18, 20, 22, 25, 28, 80, 19],
                       [10, 12, 14, 16, 15, 13, 11]])
print("Shape:", smart_grid.shape)
print("Average current per line", np.mean(smart_grid, axis=1))
print("Max smart grid:", np.max(smart_grid))
print("Min smart grid:", np.min(smart_grid))
print("Stability grid per line:", np.std(smart_grid, axis=1))
print("Stability grig", np.std(smart_grid))
print("reading line3 and hour5", smart_grid[2,4])
print("Readings from line5:", smart_grid[4])
print("Hour4 readings from all lines:", smart_grid[:,3])
print("Peak hours3 to 6 fo all lines:", smart_grid[:, 2:5])
print("Normal operations:", smart_grid * 1.1)
print("Fault surge:", smart_grid * 2)
print("Reshape smart grid:", smart_grid.reshape(7,6))
np.savetxt("fault_detection.csv", smart_grid, delimiter=",")
print("File saved!")
loaded_smartgrid = np.loadtxt("fault_detection.csv", delimiter=",")
print("Loaded smart grid", loaded_smartgrid)
print("Max current per line from loaded smart grid:", np.max(loaded_smartgrid, axis=1))



# CHALLENGE4:
solar = np.array([[150, 280, 420, 550, 600, 580, 450, 300, 160], 
                  [140, 270, 410, 540, 590, 570, 440, 290, 150], 
                  [160, 290, 430, 560, 610, 590, 460, 310, 170],
                  [120, 250, 390, 520, 570, 550, 420, 270, 140],
                  [155, 285, 425, 555, 605, 585, 455, 305, 165],
                  [10, 20, 30, 500, 550, 530, 400, 250, 100],
                  [145, 275, 415, 545, 595, 575, 445, 295, 155]])

print("Shape:", solar.shape)
print("Average output per panel:", np.mean(solar, axis=1))
print("Max solar:", np.max(solar))
print("Min solar:", np.min(solar))
print("Stability:", np.std(solar, axis=1))
print("Total energy output:", np.sum(solar))
print("All readings from panel6:", solar[5, :])
print("Reading at panel6 hour1 and hour2:", solar[5, 0:2])
print("Hour5 readings from all apnel:", solar[:, 4])
print("Increase efficiency:", solar * 1.05)
print("Cloud cover output:", solar * 0.7)
print("Reshaped:", solar.reshape(9, 7))
np.savetxt("solar_farm_report.csv", solar, delimiter=",")
print("File saved!")
loaded_solar = np.loadtxt("solar_farm_report.csv", delimiter=",")
print("Loaded:", loaded_solar)
print("Average output per panel loaded solar:", np.mean(loaded_solar, axis=1))