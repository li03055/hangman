def arrow(my_char, max_length):
    arrow = ""
    for i in range(1, max_length + 1):
        arrow += my_char * i + "\n"
    for i in range(max_length - 1, 0, -1):
        arrow += my_char * i + "\n"
    return arrow


def main():
    print(arrow('* ', 5))

if __name__ == "__main__":
    main()