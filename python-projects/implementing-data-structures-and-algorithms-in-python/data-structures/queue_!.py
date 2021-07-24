# # implementing a queue using 2 stacks
# class Queue:
#     def __init__(self):
#         # queue will be s1
#         self.s1 = []
#         # buffer would be s2
#         self.s2 = []

#     def enqueue(self, x):
#         # move all elements in s1 to s2
#         while len(self.s1) != 0:
#             self.s2.append(self.s1.pop())
#         # push new element into s1 (bottom)
#         self.s1.append(x)
#         # move all elements back into s1 from s2
#         while len(self.s2) != 0:
#             self.s1.append(self.s2.pop())

#     def dequeue(self):
#         # check if s1 is empty
#         if len(self.s1) == 0:
#             return "Empty queue"
#         # return the top element from s1
#         return self.s1.pop()

# implementing queue using a list (not efficient since it doesn't have a capacity)

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, val):
        self.queue.append(val)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return False
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

#tests
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(f"Size: {q.size()}")
