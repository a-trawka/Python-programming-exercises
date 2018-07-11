"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


def count_upper(sequence):
    f = filter(lambda x: x.isupper(), sequence)
    return f'UPPER CASE {len(list(f))}'


def count_lower(sequence):
    f = filter(lambda x: x.islower(), sequence)
    return f'LOWER CASE {len(list(f))}'


sequence = 'Hello world!'
print(count_upper(sequence))
print(count_lower(sequence))
