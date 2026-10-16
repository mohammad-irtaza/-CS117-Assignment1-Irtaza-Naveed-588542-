def parallel_resistance(resistors):
    sum_of_inverses= 0
    for resistor in resistors:
        sum_of_inverses = sum_of_inverses + 1 / resistor
    return round(1 / sum_of_inverses, 2)
print("parallel_resistance([5, 5]) ->", parallel_resistance([5,7]))
print("parallel_resistance([4400,3290,600]) ", parallel_resistance([5466,655,765]))
