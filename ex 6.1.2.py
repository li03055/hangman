def shift_left(my_list):
    return my_list[1:] + [my_list[0]]

def main():
    print(shift_left([0, 1, 2]))


if __name__ == "__main__":
    main()