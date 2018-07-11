"""
Write a program that computes the net amount of
a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""


def parse_log(log):
    sign, amount = log.split(' ')
    if sign == 'D':
        return int(amount)
    elif sign == 'W':
        return -int(amount)


def compute_balance(logs):
    return sum(map(parse_log, logs.split('\n')))


if __name__ == '__main__':
    logs = 'D 300\nD 300\nW 200\nD 100'
    print(compute_balance(logs))
