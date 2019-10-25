import time

def iterative(digit, degree):
    if degree == 1:
        return digit
    else:
        return digit * iterative(digit, degree - 1)

def degreeSecondMultiplication(digit, degree):
    binDegree = bin(degree).__str__().replace('0b', '')
    preLast = len(binDegree) - 1
    result = 1
    for it in range(len(binDegree)):
       Sign = binDegree[it]
       if it == preLast:
           result *= digit
       elif Sign == 0:
           result = result ** 2
       else:
           result *= digit ** 2

    return result
if __name__ == '__main__':
    print('Please input digit:')
    digit = input()
    print('Please input degree:')
    degree = input()
    start = time.time()
    #result = iterative(int(digit), int(degree))
    result = degreeSecondMultiplication(int(digit), int(degree))
    stop = time.time()
    print(result, start, stop, stop - start)