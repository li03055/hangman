def squared_numbers(start, stop):
    squares_list = []
    while start <= stop:
        squares_list.append(start ** 2)
        start += 1
    return squares_list

def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))

if __name__ == '__main__':
    main()