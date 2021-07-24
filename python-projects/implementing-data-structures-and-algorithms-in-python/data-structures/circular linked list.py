class Node():
    # basic node class
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList():
    # New linked list class with methods
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def append(self, data):
        # if nothing is in the CLL yet, make a new node point to itself
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        # else move to tail and insert the new node there, and set the next to the head
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
        self.size += 1

    def prepend(self, data):
        # if nothing is in the CLL yet, make a new node point to itself
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            current_node = self.head
            # go to tail and insert new node after it
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node
        self.size += 1

    def __str__(self):
        list_string = ""
        current_node = self.head
        while current_node:
            list_string += str(current_node.data)
            list_string += ", "
            current_node = current_node.next
            if current_node == self.head:
                return list_string

    def remove(self, val):
        # removing a node while assuming all nodes
        # in the CLL are unique
        if self.head:
            current_node = self.head
            # check if the head data matches val
            if self.head.data == val:
                # move till the tail of the CLL
                while current_node.next != self.head:
                    current_node = current_node.next
                # case where there's only one node and that gets removed
                if self.head == self.head.next:
                    self.head = None
                # set tail next and head to current head's next
                else:
                    current_node.next = self.head.next
                    self.head = self.head.next
            else:
                previous_node = None
                # traverse till the tail node, and remove the node if the value is matched
                while current_node.next != self.head:
                    previous_node = current_node
                    current_node = current_node.next
                    if current_node.data == val:
                        previous_node.next = current_node.next
                        current_node = current_node.next
        self.size -= 1

    # # josephus elimination problem where n is the number of steps in each elimination
    # # it returns the last remaining person. k is the number of people to put in CLL
    # def josephus(self, n, k):
    #     # while true iterate over CLL n times, remove current member from list
    #     # if self.size == 1: return self.head
    #     # populate CLL with k people
    #     for i in range(1, k+1):
    #         self.append(i)
    #     print(self)
    #     current_node = self.head
    #     while (self.size > 1):
    #         # iterate over CLL n times
    #         for i in range(n):
    #             current_node = current_node.next
    #         removed_node = current_node
    #         current_node = current_node.next
    #         self.remove(removed_node.data)
    #         # print(self)
    #     return str(self.head.data)


def main():
    test_list = CircularLinkedList()
    # for i in range(10):
    #     test_list.append(i)
    # for i in range(10, 20):
    #     test_list.prepend(i)
    # print(test_list)

    # josephus has issues
    # test_list = CircularLinkedList()
    # print(test_list.josephus(2, 4))
    # test_list = CircularLinkedList()
    # print(test_list.josephus(3, 5))


main()
