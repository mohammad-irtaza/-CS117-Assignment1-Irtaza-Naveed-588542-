def load_divider(vs, r1, r2, rl):
    unloaded_voltage =vs*r2/(r1+r2)
    r2_with_load=(r2*rl)/(r2 +rl)
    load_voltage = vs * r2_with_load / (r1 + r2_with_load)
    return unloaded_voltage,load_voltage
print("loaded_divider(18,1980,1676,200)",load_divider(14,1967,1555,567))
