volt= [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
best= 1
best_start= 0
current= 7
current_start= 0
for i in range(1, len(volt)):
    if volt[i] < volt[i - 1]:
        current= current+1
    else:
        current= 7
        current_start= i
    if current> best:
        best= current
        best_start= current_start

best_end= best_start+ best- 1
print("longest continuous drop:", best,"minutes")
print("start at:", volt[best_start],"V")
print("ended at:", volt[best_end],"V")
