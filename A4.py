bit_a = int(input("Enter A: "))
bit_b = int(input("Enter B: "))

if (bit_a != 0 and bit_a != 1) or (bit_b != 0 and bit_b != 1):
    print("bits can only be 0 or 1")
else:
    if bit_a == 1 and bit_b == 1:
        and_result = 1
    else:
        and_result = 0
    if bit_a == 1 or bit_b == 1:
        or_result = 1
    else:
        or_output = 0
    if bit_a != bit_b:
        xor_result = 1
    else:
        xor_result = 0
    print("AND=", and_result)
    print("OR=", or_output)
    print("XOR=", xor_result)
