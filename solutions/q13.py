"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


def letters(sequence):
    f = filter(lambda x: x.isalpha(), sequence)
    return f'LETTERS {len(list(f))}'


def digits(sequence):
    f = filter(lambda x: x.isdigit(), sequence)
    return f'DIGITS {len(list(f))}'


sequence = 'hello world! 123'
print(letters(sequence))
print(digits(sequence))


