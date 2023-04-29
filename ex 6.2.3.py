def format_list(my_list):
    evens = my_list[::2]
    last = " and " + my_list[-1]
    return ", ".join(evens) + last

def main():
    list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    new_list = format_list(list)
    print(new_list)

if __name__ =='__main__':
    main()