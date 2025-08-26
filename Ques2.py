binary_input = input("Enter binary number: ")
ones = binary_input.count('1')
zeros = binary_input.count('0')
output = '1' * ones + '0' * zeros
print("Output:", output)
