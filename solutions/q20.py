"""
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
"""


class MultiplesOfSevenGenerator:

    def __init__(self, n):
        self.sequence = range(n + 1)

    def __iter__(self):
        for number in self.sequence:
            if not number % 7:
                yield number


msg = MultiplesOfSevenGenerator(106)
for n in msg:
    print(n)

