import math


def catalan(n):
    return int(math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))


for i in range(10):
    print(catalan(i), end=" ")
