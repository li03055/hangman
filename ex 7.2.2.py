import string

def numbers_letters_count(my_str):
    count_nums = 0
    count_chars = 0
    for char in my_str:
        if char.isdigit():
            count_nums += 1
        elif char.isalpha() or char.isspace() or char in string.punctuation:
            count_chars += 1
    return [count_nums, count_chars]



def main():
    print(numbers_letters_count("Python 3.6.3"))

if __name__ == '__main__':
    main()