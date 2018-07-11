"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""


def divisible_by_5(number):
    binary = int(number, 2)
    if not binary % 5:
        return number


for n in '0100,0011,1010,1001'.split(','):
    result = divisible_by_5(n)
    if result:
        print(result)
