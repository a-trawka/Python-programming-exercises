"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""


def extend_to_n(digit, n):
    return int(n * str(digit))


def sum_sequence(digit):
    sequence = [extend_to_n(digit, n) for n in range(1, 5)]
    return sum(sequence)


print(sum_sequence(9))
