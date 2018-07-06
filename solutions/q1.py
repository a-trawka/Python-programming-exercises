"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def check(start, end):
    for number in range(start, end):
        if not number % 7 and number % 5:
            print(f'{number},', end='')


check(2000, 3001)
