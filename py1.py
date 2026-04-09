def add_binary(a, b):
    decimal_sum = int(a, 2) + int(b, 2)
    return bin(decimal_sum)[2:]

# Example
print(add_binary("1011", "110"))