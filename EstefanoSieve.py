def createSieve(value):
    return [it  for it in range(1, value + 1) if value % it == 0]

def computeEstafanoSieve(first, second):
    first, second = [second, first] if first < second else [first, second]
    sieveEstefanoSecond = createSieve(second)
    print([it for it in sieveEstefanoSecond if first % it == 0])

if __name__ == '__main__':
    print('Input first value:')
    first = input()
    print('Input second value:')
    second = input()
    computeEstafanoSieve(int(first), int(second))