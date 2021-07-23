class CircularQueue:
    def __init__(self, k: int):
        self.queue = [None for i in range(k)]
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        # check if queue is full (rear is right behind front)
        if self.isFull():
            print("Queue is Full")
            return

        # check if queue is empty
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            # adjust rear and add value to queue
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        # check if queue is empty
        if self.isEmpty():
            print("Queue is Empty")
            return
        # case where only one element exists
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = self.rear = -1
        else:
            # shift front to next element in queue
            temp = self.queue[self.front]
            self.front = (self.front+1) % self.size
        return temp


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

#tests
if __name__ == '__main__':
    q = CircularQueue(2)
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
