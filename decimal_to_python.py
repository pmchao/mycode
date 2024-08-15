def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def decimal_to_hex(n):
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hex_representation = ""
    while n > 0:
        hex_representation = hex_digits[n % 16] + hex_representation
        n = n // 16
#     return hex_representation

# Example usage
#decimal_number = int(input("Enter a decimal number: "))
decimal_number=26



#binary_representation = decimal_to_binary(decimal_number)
hex_representation = decimal_to_hex(decimal_number)

#print(f"The binary representation of {decimal_number} is {binary_representation}")
print(f"The hexadecimal representation of {decimal_number} is {hex_representation}")
