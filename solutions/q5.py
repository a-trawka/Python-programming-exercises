"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class ReallyDumbClass:

    def __init__(self):
        self.txt = ''

    def get_string(self):
        self.txt = input('Input text: ')

    def print_string(self):
        print(self.txt.upper())


if __name__ == '__main__':
    rdc = ReallyDumbClass()
    rdc.print_string()
    rdc.get_string()
    rdc.print_string()
