"""
Stack Data Structure.
"""
class Stack():
    # Core methods
    def __init__(self):
        # Initializes stack with a list class variable
        self.items = []

    def push(self, item):
        # Appends item to stack when function is called
        self.items.append(item)

    def pop(self):
        # Removes the top element in the stack and returns it
        return self.items.pop()

    def peek(self):
        # Returns top element if stack is not empty
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    # Other helpful methods
    def get_stack(self):
        return self.items

    def __str__(self):
        # Returns string representation of stack
        return str(stack_1.get_stack())


stack_1 = Stack()
for i in range(5):
    stack_1.push(i)
print(stack_1)
for j in "abcde":
    stack_1.push(j)
print(stack_1)
for k in range(7):
    stack_1.pop()
print(stack_1)
print(stack_1.is_empty())
print(stack_1.peek())
