from builtins import int

import math

def findReminder(large, small):
    tmp = large / small
    if tmp == 1:
        return small, 0
    elif tmp == large:
        return 1, 0
    else:
        mainPart = round(tmp - 0.5)
        result = large - mainPart * small
        return small, result

if __name__ == "__main__":
    print('Please, input first digit:')
    first = input()
    print('Please, input second digit:')
    second = input()
    if first < second:
        first, second = second, first
    while second:
        first, second = findReminder(int(first), int(second))
    print('The Grsatest divider is ', first)