from queue import Queue

# # stack of plates
# class SetOfStacks():
#     def __init__(self, size):
#         self.stacks = []
#         self.size = size

#     def push(self, data):
#         if len(self.stacks) == 0:
#             self.stacks.append([])
#         top = self.stacks[-1]
#         if len(top) == self.size:
#             new_stack = []
#             self.stacks.append(new_stack)
#             new_stack.append(data)
#             return True
#         else:
#             top.append(data)
#             return True

#     def pop(self):
#         # return false if stack is empty
#         if len(self.stacks) == 0:
#             return False
#         top = self.stacks[-1]
#         data = top.pop()
#         # pop stack from stacks if it is empty
#         if len(top) == 0:
#             self.stacks.pop()
#         return data

# sos = SetOfStacks(5)
# for i in range(15):
#     sos.push(i)
# print(sos.stacks)
# for i in range(5):
#     print(sos.pop())
# print(sos.stacks)


# # Queue via Stacks
# class MyQueue():
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def enQueue(self, data):
#         # add new data to first stack
#         self.s1.append(data)

#     def deQueue(self):
#         # move all data from first stack to second stack (reverses order)
#         while len(self.s1) != 0:
#             self.s2.append(self.s1.pop())
#         # pop the earliest data (top of second stack)
#         data = self.s2.pop()
#         # move everything from second stack to first
#         while len(self.s2) != 0:
#             self.s1.append(self.s2.pop())
#         return data

# q = MyQueue()
# for i in range(10):
#     q.enQueue(i)
# for i in range(10):
#     print(q.deQueue())


# # Sort Stack
# def sort_stack(stack):
#     sorted_stack = []
#     while len(stack) != 0:
#         # check if top element in stack is more than top in sorted stack
#         # if it is less, pop top of sorted stack and push it to stack
#         temp = stack.pop()
#         if len(sorted_stack) == 0:
#             sorted_stack.append(temp)
#         else:
#             while sorted_stack[-1] > temp:
#                 stack.append(sorted_stack.pop())
#             sorted_stack.append(temp)
#     return sorted_stack



# my_stack = [1, 5, 3, 2, 7, 8, 1]
# print(sort_stack(my_stack))

# # Animal Shelter
# class AnimalShelter:
#     def __init__(self):
#         self.animals = []

#     def enqueue(self, specie):
#         new_animal = Animal(specie)
#         self.animals.append(new_animal)

#     def dequeueAny(self):
#         return self.animals.pop(0)

#     def dequeueCat(self):
#         for index, animal in enumerate(self.animals):
#             if animal.specie == "cat":
#                 return self.animals.pop(index)

#     def dequeueDog(self):
#         for index, animal in enumerate(self.animals):
#             if animal.specie == "dog":
#                 return self.animals.pop(index)

# class Animal:
#     def __init__(self, specie):
#         self.specie = specie

#     def __str__(self):
#         return f"{self.specie} animal"

# my_shelter = AnimalShelter()
# my_shelter.enqueue("cat")
# my_shelter.enqueue("cat")
# my_shelter.enqueue("dog")
# my_shelter.enqueue("cat")
# my_shelter.enqueue("dog")
# my_shelter.enqueue("cat")
# my_shelter.enqueue("dog")
# print(my_shelter.dequeueAny())
# print(my_shelter.dequeueCat())
# print(my_shelter.dequeueDog())
# for animal in my_shelter.animals:
#     print(animal, end=", ")
