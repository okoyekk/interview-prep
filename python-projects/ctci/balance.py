def balance_string(test):
    # Balancing a string using a stack that holds indices of parentheses
    # And a dctionary that maps brackets to each other
    # Time complextity of O(n) where n: test [string]
    stack = []
    matches = {"]": "[", ")": "(", "}": "{"}
    unbalanced_indices = []
    new_string = ""
    for i in range(len(test)):
        if test[i] in matches.keys():
            if len(stack) == 0:
                unbalanced_indices.append(i)
            else:
                if test[stack[-1]] != matches[test[i]]:
                    unbalanced_indices.append(i)
                else:
                    unbalanced_indices.remove(stack.pop())
        elif test[i] in matches.values():
            stack.append(i)
            unbalanced_indices.append(i)

    for index, element in enumerate(test):
        if index not in unbalanced_indices:
            new_string += element
    print("=============")
    print(f"old: {test}")
    return f"new: {new_string}"


test_strings = ["[({(jojo)}siwa)[]}", "(([{jojo([]}]))", "[[[{{}}]]]"]
for string in test_strings:
    print(balance_string(string))
