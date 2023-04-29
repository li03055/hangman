def count_chars(my_str):
    char_dict = {}
    for char in my_str:
        if char != ' ':
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))

if __name__ == '__main__':
    main()


