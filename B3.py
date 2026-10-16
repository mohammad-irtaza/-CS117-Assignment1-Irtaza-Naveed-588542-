reads= (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
above_count = 0
highest=reads[0]
lowest=reads[0]
total=0
for read in reads:
    if read> 3.2:
        above_count = above_count + 1
    if read>highest:
        highest=read
    if read<lowest:
        lowest=read
    total=total +read
average =total/2
print("readings above 3.2 V:",above_count)
print("highest:",highest,"V")
print("lowest:",lowest, "V")
print("Average:",round(average,2),"V")
