class Node():
    # Node Class
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    # Linked list class with standard and extra methods
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        # New node's next pointer is set to the current head
        new_node = Node(data, self.head)
        # current head is set to the new node
        self.head = new_node
        # Linked list size is incremented by 1
        self.size += 1

    def remove_node(self, data):
        current_node = self.head
        previous_node = None

        while current_node:
            # Path if data to be removed is the head
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node
                self.size -= 1
                return True  # Remove successful
            # Path if data to be removed is in between the linked list
            else:
                # Previous node is set to the current node, and the
                # Current node is set to the next.
                previous_node = current_node
                current_node = current_node.next
        return False  # Remove unsucessful

    def find_node(self, data):
        current_node = self.head
        while current_node:
            # Returns the current node's data whenever it os the same as
            # what is to be found
            if current_node.data == data:
                return(data)
            # Moves to the next node if not
            else:
                current_node = current_node.next
            # While loop ends when self.next is == None
            # Because the current node changes to None due to the nextunction)
            # in the else block above.
        # Returns none if not found
        return None

    def __str__(self):
        current_node = self.head
        link_string = ""
        size = self.get_size()
        for i in range(size):
            current_value = str(current_node.data)
            if i != size - 1:
                link_string += current_value + ", "
            else:
                link_string += current_value + "."
            current_node = current_node.next
        return link_string

    def reverse(self):
        previous_node = None
        current_node = self.head
        while(current_node):
            next_node = current_node.next
            # set the next of the current node to the previous node
            current_node.next = previous_node
            # set the previous node to the current node and set the current to the next node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


def main():
    test_list = LinkedList()
    for i in range(10):
        test_list.add_node(i)
    print(test_list)
    test_list.reverse()
    print(test_list)


main()
