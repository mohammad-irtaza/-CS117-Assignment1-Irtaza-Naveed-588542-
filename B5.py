one_percent_count=0
five_percent_count=0
reject=0
measure=float(input("enter measured resistance:"))
while measure!= 0:
    if 99.0<= measure<= 101.0:
        one_percent_count = one_percent_count + 1
    elif 95.0<= measure<= 105.0:
        five_percent_count = five_percent_count + 1
    else:
        reject= reject+1
        measured = float(input("Enter measured resistance: "))
print("1% tolerance:", one_percent_count)
print("5% tolerance:", five_percent_count)
print("Rejected:", reject)
