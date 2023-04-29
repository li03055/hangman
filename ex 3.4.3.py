string = input("Please enter a string: ")
half_length = len(string) // 2
new_string = string[:half_length].lower() + string[half_length:].upper()
print(new_string)