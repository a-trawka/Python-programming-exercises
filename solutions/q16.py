"""
Use a list comprehension to square each odd number in a list.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1, 2, 9, 4, 25, 6, 49, 8, 81
"""


def is_odd(x):
    return x % 2


def sqr_if_odd(x):
    return x ** 2 if is_odd(x) else x


def main(numbers):
    return list(map(sqr_if_odd, numbers))


if __name__ == '__main__':
    print(main([1, 2, 3, 4, 5, 6, 7, 8, 9]))
