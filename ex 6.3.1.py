def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    are_lists_equal(list1, list2)

if __name__ == '__main__':
    main()