volt = float(input("enter voltage: "))
resist = float(input("enter resistance: "))
if resist <= 0:
    print("Invalid resistance")
else:
    current = volt/resist
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
