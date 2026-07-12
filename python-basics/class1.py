#WHAT IS A VARIABLE? A variable is just a box that holds a value.
#example
voltage = 240
current = 20
resistance = 5
coursework = ("python")
print(coursework)
print(voltage)
print(resistance)

# types of data
#int(whole numbers)  240,50,35,3728
#float(decimal numbers) 24.5,3.8,240.0
#string(texts in quotes)   "Electrical engineering","python"
#boolean(true or false)  true, false
my_int = 25
my_float = 38.7
my_string = "python"
my_boolean = True
print(my_int)
print(my_boolean)
print(my_float)
print(my_string)

#Doing maths with variables
#  (*means multiply), (+means addition), (/means division), (-means subtraction)
#DOING MATHS WITH VARIABLES

voltage = 240
current = 15
primary_turns = 2500
secondary_turns = 500
transformer_turn_ratio = primary_turns/secondary_turns 
power = (voltage*current)
resistance = (voltage/current)
print(power)
print(resistance)
print(transformer_turn_ratio)

#IF/ELSE (MAKING DECISIONS)

voltage = 240
if voltage > 250:
    print("WARNING! - Voltage is too high")
else:
    print("SAFE")
if voltage < 100:
    print("WARNING! - Volatge is too low")
else:
    print("SAFE!")
if voltage == 240:
    print("SAFE!")
#INSTEAD OF WRITING 3 SEPERATE IF/ELSE BLOCKS WE CAN COMBINE THEM WITH "ELIF"
#EXAMPLE
voltage = 240
if voltage > 250:
    print("WARNING! - Volatge is high")
elif voltage < 100:
    print("WARNING! - Voltage is low")
else:
    print("SAFE!")

#BOOLEAN: ABOOLEAN IS THE VALUE OF ONLY ONE OF TWO THINGS TRUE OR FALSE.
#BOOLEANS CAN BE WRITTEN IN TWO WAYS;
#WAY 1: TYPE IT DIRECTLY
is_motor_running = True
is_circuit_broken = False
#WAY 2: MAKE A COMPARISON; WHEN YOU COMPARE TWO THINGS PYTHON AUTOMATICALLY GIVES TRUE OR FALSE.
voltage = 230
result1 = voltage < 250
result2 = voltage > 250
print(result1)
print(result2)
# comparison signs
# (<)  less than
# (>)  greater than
# (==) equals to
# (!=) not equals to
# (<=) less than or equals to
# (>=) greater than or equals to
#remember that (=) means set the value while (==) means equals to

voltage = 230
max_voltage = 250
is_safe = voltage < max_voltage
is_high = voltage > max_voltage
is_exactly_max = voltage == max_voltage
print(is_safe)
print(is_high)
print(is_exactly_max)