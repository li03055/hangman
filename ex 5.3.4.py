def last_early(my_str):
    last_letter = my_str[-1]
    if last_letter in my_str[:-1] or last_letter.upper() in my_str[:-1]:
        return True
    else:
        return False


