def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n

def fact(n):
    if (n <= 1):
        return 1
    else:
        return n * fact(n - 1)


print(sum(5))
print(fact(5))
