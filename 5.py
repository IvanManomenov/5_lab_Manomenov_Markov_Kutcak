class NotEnoughSpace(Exception):
    def print(self):
        print("Недостаточно пространства")

class EmptyStack(Exception):
    def print(self):
        print("Попытка использовать пустой стек")


class stackx():
    def __init__(self):
        self.stackSize = 100
        self.buffer = [self.stackSize * 3]
        self.stackPointer = {0, 0, 0}


    def push(self, stackNum, value):
        try:
            if (self.stackPointer[stackNum] >= self.stackSize):
                raise NotEnoughSpace()
        except NotEnoughSpace as nf:
            nf.print()
        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum] + 1
            self.stackPointer[stackNum] += 1
            self.buffer[index] = value


    def pop(self, stackNum):
        try:
            if (self.stackPointer[stackNum] == 0):
                raise EmptyStack()
        except EmptyStack as nf:
            nf.print()
        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum]
            self.stackPointer[stackNum] -= 1
            value = self.buffer[index]
            self.buffer[index] = 0
            return value


    def peek(self, stackNum):
        index = stackNum * self.stackSize + self.stackPointer[stackNum]
        return self.buffer[index]

    def isEmpty(self, stackNum):
        return self.stackPointer[stackNum] == 0