def is_greater(my_list, n):
    greater = []
    for num in my_list:
        if num > n:
            greater.append(num)
    return greater


def main():
    print(is_greater([1, 30, 25, 60, 27, 28], 28))

if __name__ == '__main__':
    main()