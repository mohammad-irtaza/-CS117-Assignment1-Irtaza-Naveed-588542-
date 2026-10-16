color = input("Enter band colour: ").lower()
if color =="black":
 digit = 0
elif color =="brown":
 digit = 1
elif color =="red":
 digit = 2
elif color =="orange":
 digit = 3
elif color =="yellow":
 digit = 4
elif color =="green":
 digit = 5
elif color =="blue":
 digit = 6
elif color =="violet":
 digit = 7
elif color =="grey":
 digit = 8
elif color =="white":
 digit = 9
else:
    digit = None

if digit is None:
    print("Invalid color")
else:
    print("digit =",digit)
