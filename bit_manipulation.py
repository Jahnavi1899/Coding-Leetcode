def swap_numbers(a, b):
    # any number XOR itself will result in a 0 and any number XOR 0 will result in the same number

    a = a ^ b
    b = b ^ a # (b ^ a ^ b)
    a = a ^ b # (a ^ b ^ a)

    return a, b

a, b = 10, 15
a ,b = swap_numbers(a, b)
print(a, b)
