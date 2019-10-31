import random

def selectionSort(Array):
    lenOfList = len(Array)
    for itMain in range(0, lenOfList):
        min = itMain
        for itSlave in range(itMain, lenOfList):
            if Array[min] > Array[itSlave]:
                min = itSlave
        if min != itMain:
            tmp = Array[itMain]
            Array[itMain] = Array[min]
            Array[min] = tmp

def bubbleSort(array):
    lenOfList = len(array)
    for itMain in range(lenOfList - 1):
        for itSlave in range(0, lenOfList - itMain):
            if itSlave + 1 == lenOfList:
                continue
            if array[itSlave] > array[itSlave + 1]:
                tmp = array[itSlave]
                array[itSlave] = array[itSlave + 1]
                array[itSlave + 1] = tmp

def insertionSort(array):
    for itMain in range(1, len(array)):
        curValue = array[itMain]
        itSlave = itMain
        while(itSlave > -1 and curValue < array[itSlave - 1]):
            itSlave -= 1
        itSlave = 0 if itSlave == -1 else itSlave
        if itSlave != itMain:
            array.insert(itSlave, curValue)
            array.__delitem__(itMain + 1)

def sortSubPart(array, left, right):
    pivot = array[right]
    i = left
    for it in range(left,right):
        if array[it] <= pivot:
           tmp = array[it]
           array[it] = array[i]
           array[i] = tmp
           i += 1
    tmp = array[i]
    array[i] = array[right]
    array[right] = tmp
    return i

def quickSort(array, left, right):
    if left < right:
        pivot = sortSubPart(array, left, right)
        quickSort(array, left, pivot - 1)
        quickSort(array, pivot + 1, right)


def shellSort(array):
    increment = len(array) // 2
    while increment > 0:

        for startPosition in range(increment):
            gapInsertionSort(array, startPosition, increment)

        print("После инкрементации размера на", increment, "массив:", array)

        increment //= 2


def gapInsertionSort(array, low, gap):
    for i in range(low + gap, len(array), gap):
        currentvalue = array[i]
        position = i

        while position >= gap and array[position - gap] > currentvalue:
            array[position] = array[position - gap]
            position = position - gap

        array[position] = currentvalue

def heapSort(array):

    def shiftDown(parent, length):
        nonlocal array
        item = array[parent]
        while True:
            child = (parent << 1) + 1
            if child >= length:
                break
            if child + 1 < length and array[child] < array[child + 1]:
                child += 1
            if item < array[child]:
                array[parent] = array[child]
                parent = child
            else:
                break
        array[parent] = item

    length = len(array)
    for it in range((length >> 1) - 1, -1, -1):
        shiftDown(it, length)

    for it in range(length - 1, 0, -1):
        array[0], array[it] = array[it], array[0]
        shiftDown(0, it)


class BtreeFind:
    def __init__(self, key = None):
        self._key = key
        self._leftTree = None
        self._rightTree = None

    def insertElement(self, key):
        if self._key == None:
            self._key = key
        elif self._key > key:
            if self._leftTree == None:
                self._leftTree = BtreeFind(key)
            else:
                self._leftTree.insertElement(key)
        elif self._key <= key:
            if self._rightTree == None:
                self._rightTree = BtreeFind(key)
            else:
                self._rightTree.insertElement(key)

    def insertList(self, lst):
        for elLst in lst:
            self.insertElement(elLst)

    @staticmethod
    def printTree(Node):
        #leftestNode = self.findLeftestNodeBTree()
        #return leftestNode.fillLst()
        lstLeft = [] if Node._leftTree == None else Node.printTree(Node._leftTree)
        lstRigth = [] if Node._rightTree == None else Node.printTree(Node._rightTree)
        return lstLeft + [Node._key] + lstRigth

def mergeSort(array):
    if len(array) == 1:
        return array
    pivot = len(array) >> 1
    leftPart = array[0:pivot]
    rightPart = array[pivot:]
    leftPart = mergeSort(leftPart)
    rightPart = mergeSort(rightPart)
    for valueRight in rightPart:
       insert = False
       for itLeft in range(0, len(leftPart)):
          if valueRight <= leftPart[itLeft]:
              insert = True
              leftPart.insert(itLeft, valueRight)
              break
       if not insert:
           leftPart.append(valueRight)
    return leftPart

if __name__ == "__main__":
    array = [5,3,4,5,1,9,8,7]
    mas = {it:0 for it in range(1,11)}
    array = []
    for it in range(1000):
      array.append(random.randint(1, 10))
    for it in array:
        mas[it] += 1
    print(array)
    print(mas)
    array = mergeSort(array)
    print(array)
    mas = {it: 0 for it in range(1, 11)}
    for it in array:
        mas[it] += 1
    print(mas)