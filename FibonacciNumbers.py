import math

def recursive(digit):
    if digit == 1:
        return 0
    elif digit == 2:
        return  1
    else:
        return recursive(digit - 1) + recursive(digit - 2)


def iteration(digit):
    tmp = 0
    value = 1
    oldValue = 0

    if digit == 1:
        return 0
    elif digit == 2:
        return 1
    for i in range(digit - 2):
        tmp = value
        value += oldValue
        oldValue = tmp

    return value

def computefi():
    return (1 + math.sqrt(5)) / 2

def computef():
    return (1 - math.sqrt(5)) / 2

def GoldenSection(digit):
    return int((computefi() ** digit - computef() ** digit) / math.sqrt(5))

def multiplicateMatrice(matric, lastMul):
    pass

def MultiplicationMatrices(digit):
    matric = [[0, 1], [1, 1]]
    lastMul  = [0,1]
    for it in range(digit - 1):
        multiplicateMatrice(matric, matric)
    return multiplicateMatrice(matric, lastMul)

if __name__ == "__main__":
    print('Please input the position number of the sequence Euclid:')
    numberPosition = int(input())
    print(GoldenSection(numberPosition))