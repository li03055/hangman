def mult_tuple(tuple1, tuple2):
    return tuple((a, b) for a in tuple1 for b in tuple2) + tuple((b, a) for a in tuple1 for b in tuple2)

def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

if __name__ == "__main__":
    main()
