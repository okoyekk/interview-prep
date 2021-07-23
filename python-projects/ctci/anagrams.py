def is_anagram(a1, a2):
    a1_dict = {}
    for letter in a1:
        if letter not in a1_dict:
            a1_dict[letter] = 1
        else:
            a1_dict[letter] += 1

    for letter in a2:
        if letter not in a1_dict:
            return False
        else:
            a1_dict[letter] -= 1

    for v in a1_dict.values():
        if v != 0:
            return False
    return True

def main():
    print(is_anagram("fried", "fired")) # True
    print(is_anagram("fried", "fird")) # False
    print(is_anagram("1233", "1323")) # True
    print(is_anagram("1433", "1324")) # False


main()
