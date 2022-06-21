class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.cur_len = 0
        self.length = k
        self.head, self.tail = 0, -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.length
        self.data[self.tail] = value
        self.cur_len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.length
        self.cur_len -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.cur_len == 0

    def isFull(self) -> bool:
       return self.cur_len == self.length         


obj = MyCircularQueue(3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
breakpoint()
obj.deQueue()
obj.Front()
obj.Rear()
obj.isEmpty()
obj.isFull()

