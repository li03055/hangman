def seven_boom(end_number):
    string = "BOOM"
    list = []
    for x in range(end_number + 1):
        if x % 7 == 0 or '7' in str(x):
            list.append(string)
        else:
            list.append(x)
    return list





def main():
    print(seven_boom(17))

if __name__ == '__main__':
    main()