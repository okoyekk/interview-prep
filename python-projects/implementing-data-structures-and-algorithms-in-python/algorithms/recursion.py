def sum(n):
    """Sums all numbers up to a number and returns it"""
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n


def fact(n):
    """Returns the factorial of a number"""
    if (n <= 1):
        return 1
    else:
        return n * fact(n - 1)

def print_reverse(string):
    """Prints a string in reverse order"""
    print_reverse_helper(string, 0)

def print_reverse_helper(string, start):
    """Helper function for print reverse"""
    if start == len(string) or len(string) == 0:
        return
    print_reverse_helper(string, start + 1)
    print(string[start], end="")


# print(sum(5))
# print(fact(5))

name = "kenechi"
print(name)
print_reverse(name)
print()
