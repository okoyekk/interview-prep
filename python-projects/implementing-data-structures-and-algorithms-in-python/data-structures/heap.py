class MinHeap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.items = [None] * self.capacity

    # Next 3 methods get indices of an element's children/parent
    def get_left_child_index(self, index):
        return int((index * 2) + 1)

    def get_right_child_index(self, index):
        return int((index * 2) + 2)

    def get_parent_index(self, index):
        return int((index - 1) / 2)

    # Next 3 methods check if an element has children/parents
    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    # next 3 methods get the children/parent's value
    def get_left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def get_right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def get_parent(self, index):
        return self.items[self.get_parent_index(index)]

    # swap 2 elements in heap
    def swap(self, index_1, index_2):
        self.items[index_1], self.items[index_2] = self.items[index_2], self.items[index_1]

    # double size of array and copy elements over
    def ensure_extra_capacity(self):
        if self.size == self.capacity:
            extension = [None] * self.capacity
            self.items += extension
            self.capacity *= 2

    # returns the first element (parent/root) in the array if it exists
    def peek(self):
        if self.size == 0:
            print("Heap is Empty!")
            return
        return self.items[0]

    # removes minimum element from heap
    def poll(self):
        if self.size == 0:
            print("Heap is Empty!")
            return False
        # get item and replace it with last added element
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        # set last item to None and decrement self.size
        self.items[self.size - 1] = None
        self.size -= 1
        # shift elements down as required
        self.heapify_down()
        return item

    # adds a new element to heap
    def add(self, item):
        self.ensure_extra_capacity()
        # add element in the last slot in heap and increase size of heap
        self.items[self.size] = item
        self.size += 1
        # shift elements up as required
        self.heapify_up()

    # shifts the last inserted element up as required
    def heapify_up(self):
        index = self.size - 1
        # move element up heap if it has a parent and is less than the parent
        while (self.has_parent(index) and (self.get_parent(index) > self.items[index])):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    # shifts the first/root element down as required
    def heapify_down(self):
        index = 0
        # keep moving down heap as required
        while self.has_left_child(index):
            # get smaller child index between left and right(if it exists)
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and (self.get_right_child(index) < self.get_left_child(index)):
                smaller_child_index = self.get_right_child_index(index)
            # compare current index value with the smaller child and swap if needed
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

my_heap = MinHeap()
my_heap.add(10)
my_heap.add(15)
my_heap.add(20)
my_heap.add(17)
my_heap.add(25)
print(my_heap.items)
print(my_heap.poll())
print(my_heap.items)
print(my_heap.poll())
print(my_heap.items)
print(my_heap.peek())
print(my_heap.items)
