# Example variable
x = 42

# Get memory address in decimal
address_decimal = id(x)

# Get memory address in hexadecimal
address_hex = hex(id(x))

print(f"Value of x: {x}")
print(f"Memory address (decimal): {address_decimal}")
print(f"Memory address (hex): {address_hex}")
