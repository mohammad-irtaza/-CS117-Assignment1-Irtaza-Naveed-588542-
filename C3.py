def dec_to_bin(n):
    if n == 0:
        return "0"

    bin_digits = ""
    while n > 0:
        remainder = n % 2
        bin_digits = str(remainder) + bin_digits  
        n = n // 2
    return bin_digits
print("101 to binary is", dec_to_bin(101))
print("25 to binary is", dec_to_bin(25))
