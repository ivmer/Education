class TreeAVL:

    def __init__(self, key):
        self._key = key
        self._leftNode = self._rightNode = None
        self._height = 1

    def height(self):
        return self._height if self else 0

    def difference(self):
        return self._rightNode.height() if self._rightNode else 0 - self._leftNode.height() if self._leftNode else 0

    def fixHeigth(self):
        hLeft = self._leftNode._height if self._leftNode else 0
        hRight = self._rightNode._height if self._rightNode else 0
        self._height =  hLeft if hLeft > hRight else hRight + 1

    def rotateLittleRigth(self):
        leftNode = self._leftNode
        self._leftNode = leftNode._rightNode
        leftNode._rightNode = self
        self.fixHeigth()
        leftNode.fixHeigth()
        return leftNode

    def rotateLittleLeft(self):
        rightNode = self._rightNode
        self._rightNode = rightNode._leftNode
        rightNode._leftNode = self
        self.fixHeigth()
        rightNode.fixHeigth()
        return rightNode

    def balance(self):
        self.fixHeigth()
        difLeftRight = self.difference()
        if difLeftRight == 2:
            if self._rightNode.difference() < 0:
                self._rightNode = self._rightNode.rotateLittleRigth()
            return self.rotateLittleLeft()

        elif difLeftRight == -2:
            if self._leftNode.difference() > 0:
                self._leftNode = self._leftNode.rotateLittleLeft()
            return self.rotateLittleRigth()

        return self

    @staticmethod
    def insert(node, value):
        if node == None:
            return TreeAVL(value)
        if node._key > value:
            node._leftNode = TreeAVL.insert(node._leftNode, value)
        else:
            node._rightNode = TreeAVL.insert(node._rightNode, value)
        return node.balance()

if __name__ == "__main__":
    obTree = None
    for it in range(20):
        obTree = TreeAVL.insert(obTree, it)
    print(obTree.height())