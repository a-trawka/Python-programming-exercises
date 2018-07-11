"""
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def even_digits(number):
    return not any(int(l) % 2 for l in str(number))


filtered_numbers = filter(even_digits, range(2000, 3001))

for x in filtered_numbers:
    print(x)