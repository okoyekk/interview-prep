class Node():
    # DLL Node Class
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList():
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current_node = self.head
            # traverse till end of list
            while (current_node.next is not None):
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            current_node = new_node
        else:
            self.head = new_node
        # increase list size
        self.size += 1

    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
        self.size += 1

    def delete(self, del_node):
        if self.head:
            if del_node is None:
                return
            # handle case where head is to be deleted
            if self.head == del_node:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            else:
                current_node = self.head
                while (current_node.next is not None):
                    current_node = current_node.next
                    if current_node == del_node:
                        del_node.prev.next = del_node.next
                        del_node.next.prev = del_node.prev
                        break
            self.size -= 1
        else:
            print("List is empty!")

    def reverse(self):
        # swap prev and next pointers for all nodes
        if self.head:
            # case where there's only 1 node in list
            if self.head.next is None:
                return
            current_node = self.head
            # traverse till end of list and swap pointers for all
            while (current_node.next is not None):
                nxt = current_node.next
                current_node.next = current_node.prev
                current_node.prev = nxt
                current_node = nxt
            # swap tail pointers, and make it to be the head
            nxt = current_node.next
            current_node.next = current_node.prev
            current_node.prev = nxt
            self.head = current_node
        else:
            print("List is empty!")


    def __str__(self):
        current_node = self.head
        link_string = ""
        size = self.size
        for i in range(size):
            current_value = str(current_node.data)
            if i != size - 1:
                link_string += current_value + ", "
            else:
                link_string += current_value + "."
            current_node = current_node.next
        return link_string


def main():
    test_list = DoublyLinkedList()
    for i in range(10):
        test_list.append(i)
    for j in range(10, 20):
        test_list.push(j)
    for i in range(10):
        test_list.delete(test_list.head)
    print(test_list)
    test_list.reverse()
    print(test_list)


main()
