def sequence_del(my_str):
    return ''.join(char for i, char in enumerate(my_str) if char != my_str[i-1] or i == 0)





def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))

if __name__ == '__main__':
    main()