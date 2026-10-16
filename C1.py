def current(v,r):
    return v/r
def power(i,r):
    return i**2 *r
volt=30
resist=2200
current=current(volt, resist)
power=power(current, resist)
print("current =",current)
print("power =",power)
