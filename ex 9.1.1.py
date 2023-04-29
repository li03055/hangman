def are_files_equal(file1, file2):
    with open(file1, "r") as f1:
        data1 = f1.read()
    with open(file2, "r") as f2:
        data2 = f2.read()
    return data1 == data2

def main():
    print(are_files_equal("c:\words.txt", "c:\work.txt"))

if __name__ == '__main__':
    main()


