def sort_anagrams(list_of_strings):
    anagram_groups = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string].append(string)
        else:
            anagram_groups[sorted_string] = [string]
    sorted_list = [anagram_groups[key] for key in sorted(anagram_groups.keys())]
    return sorted_list


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))

if __name__ == "__main__":
    main()
