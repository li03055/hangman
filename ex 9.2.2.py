def copy_file_content(source, destination):
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        data = f1.read()
        f2.write(data)

def main():
    copy_file_content("c:\words.txt", "c:\words.txt")

if __name__ == '__main__':
    main()