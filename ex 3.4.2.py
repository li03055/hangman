string = input("Please enter a string: ")
if len(string) > 0:
    first_letter = string[0]
    new_string = first_letter + string[1:].replace(first_letter, 'e')
    print(new_string)
else:
    print("String is empty")