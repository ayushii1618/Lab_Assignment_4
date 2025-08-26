string = input("Enter a string: ")
n = int(input("Enter index to remove: "))
new_string = string[:n] + string[n+1:]
print("String after removal:", new_string)
