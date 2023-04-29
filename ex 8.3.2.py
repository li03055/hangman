my_dict = {
    "first_name": "Lior",
    "last_name": "Avraham",
    "birth_date": "03.05.2004",
    "hobbies": ["Sing", "Learn", "Go to the beach"]
}

user_input = int(input("Enter a number between 1 to 7: "))

if user_input == 1:
    print("last name: " + my_dict["last_name"])
elif user_input == 2:
    print("month birth date:n" + my_dict["birth_date"][3:5])
elif user_input == 3:
    print("num of hobbies: ")
    print(len(my_dict["hobbies"]))
elif user_input == 4:
    print("last hobby in list of hobbies is: ")
    print(my_dict["hobbies"][-1])
elif user_input == 5:
    print("adding cooking to list of hobbies: ")
    my_dict["hobbies"].append("Cooking")
    print(my_dict["hobbies"])
elif user_input == 6:
    print("turning birth_date to tuple: ")
    birth_date_tuple = tuple(map(int, my_dict["birth_date"].split(".")))
    print(birth_date_tuple)
elif user_input == 7:
    print("adding age to dict: ")
    birth_year = int(my_dict["birth_date"][-4:])
    current_year = 2023
    age = current_year - birth_year
    my_dict["age"] = age
    print(my_dict)