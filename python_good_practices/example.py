import math


def exp_taylor_term(n):
    """Return the n-th term of the exponential Taylor series."""
    return lambda x: x ** n / math.factorial(n)


term1 = exp_taylor_term(1)
term2 = exp_taylor_term(2)

print(term1(2), term2(3))

x = range(10)
y = filter(lambda x: x % 2 == 0, x)
print(list(x))
print(list(y))


def odd_or_even(x):

    switch = {
        0: "this number is even",
        1: "this number is odd",
    }
    print("{} entered: {}".format(x, switch[x % 2]))


odd_or_even(7)
