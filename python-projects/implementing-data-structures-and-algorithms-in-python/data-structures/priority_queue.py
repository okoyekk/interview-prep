from heapq import heappush, heappop, heapify

# class that models a priority queue
# (which is a queue where order depends on value of element)
class PriorityQueue:
# This implementation gives priority to smaller elements but can be changed by
# adding an additional parameter ("min" or "max") while instantiating the object
    def __init__(self, queue=[], priority="min"):
        # check if priority is valid
        if priority not in ("min", "max"):
            print("Invalid Priority!")
            return False
        self.priority = priority
        if self.priority == "max":
            # multiply all values by -1 if priority is descending
            queue = list(map(lambda x: x * -1, queue))
        heapify(queue)
        self.queue = queue

    def push(self, val):
        if self.priority == "max":
            # multiply element by -1 before adding
            # if queue priority is max (descending)
            val *= -1
        heappush(self.queue, val)
        return True

    def pop(self):
        if len(self.queue) > 0:
            val = heappop(self.queue)
            if self.priority == "max":
                # multiply top element by -1 if queue priority is max (descending)
                val *= -1
            return val
        return "Priority Queue is Empty"

    def poll(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            if self.priority == "max":
                # multiply top element by -1 if queue priority is max (descending)
                val *= -1
            return val
        return "Priority Queue is Empty"

print("Min Priority Queue")
my_queue = [6, 23, 2, 66, 1, 98, 100, 4]
min_priority_queue = PriorityQueue(my_queue)
print(min_priority_queue.poll())
print(min_priority_queue.pop())
print(min_priority_queue.pop())
min_priority_queue.push(0)
print(min_priority_queue.poll())
print("Max Priority Queue")
my_queue = [6, 23, 2, 66, 1, 98, 100, 4]
max_priority_queue = PriorityQueue(my_queue, "max")
print(max_priority_queue.poll())
print(max_priority_queue.pop())
print(max_priority_queue.pop())
max_priority_queue.push(1000)
print(max_priority_queue.poll())
