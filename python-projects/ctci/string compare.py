def compareString(string_1, string_2):
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            return False
    return True

def main():
    print(compareString("hello", "goodbye"))
    print(compareString("hello", "hello"))

main()
