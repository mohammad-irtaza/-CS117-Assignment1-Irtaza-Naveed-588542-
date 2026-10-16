how_many = int(input("How many resistors? "))
total_resistance = 0
for number in range(1, how_many + 1):
    resistor_value = float(input("Enter R" + str(number) + ": "))
    total_resistance = total_resistance + resistor_value

print("Total resistance =", total_resistance, "ohm")
