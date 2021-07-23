# # Linked List and node class
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"Node with data: {self.data}"

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def add_node(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def remove_node(self, data):
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False

    def find_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return(data)
            else:
                current_node = current_node.next
        return None

    def __str__(self):
        current_node = self.head
        list_string = ""
        while current_node:
            current_value = str(current_node.data)
            list_string += current_value + ", "
            current_node = current_node.next
        return list_string


# # Remove duplicates
# def remove_duplicates(llist):
#     # use a set to store all unique values in linked list
#     # and remove a node if the value is already in the set
#     value_set = set()
#     current = llist.head
#     previous = None
#     while current:
#         if current.data in value_set:
#             # remove node if duplicate
#             previous.next = current.next
#         else:
#             # add value to set and update previous
#             value_set.add(current.data)
#             previous = current
#         current = current.next
#     return llist.head



# duplicate_list = LinkedList()
# for i in range(10):
#     duplicate_list.add_node(i)
#     duplicate_list.add_node(i)
# print(duplicate_list)
# remove_duplicates(duplicate_list)
# print(duplicate_list)


# # Return kth to last
# def kth_to_last(llist, k):
#     # use 2 pointers to nodes, a walker and runner,
#     # where runner is k nodes away from walker
#     walker = llist.head
#     runner = llist.head
#     for i in range(k):
#         runner = runner.next
#         # check if linked list is long enough
#         if not runner:
#             print("Linked list is not long enough")
#             return False
#     # move both nodes at same speed till runner is at end of list
#     while runner.next:
#         walker = walker.next
#         runner = runner.next
#     return walker


# my_llist = LinkedList()
# for i in range(10):
#     my_llist.add_node(i)
# print(my_llist)
# print(kth_to_last(my_llist, 5))


# # Delete middle node
# def delete_middle(node):
#     # check if node is valid (not head or tail)
#     if not(node.next and node):
#         return False
#     # set current to next node's data and delete next node
#     next = node.next
#     node.data = next.data
#     node.next = next.next


# my_llist = LinkedList()
# for i in range(10):
#     my_llist.add_node(i)
# print(my_llist)
# # delete 7
# delete_middle(my_llist.head.next.next)
# print(my_llist)


# # Partition
# def partition(llist, value):
#     # make 2 linked lists, one for nodes less than
#     # value and one for nodes greater than value
#     less_list = LinkedList()
#     more_list = LinkedList()
#     current = llist.head
#     while current:
#         if current.data >= value:
#             more_list.add_node(current.data)
#         else:
#             less_list.add_node(current.data)
#         current = current.next
#     # iterate till end of less list and set next 
#     # of tail to more_list.head
#     less_ptr = less_list.head
#     while less_ptr.next:
#         less_ptr = less_ptr.next
#     less_ptr.next = more_list.head
#     return less_list
    

# my_llist = LinkedList()
# for i in (3, 5, 8, 10, 2, 1):
#     my_llist.add_node(i)
# print(my_llist)
# print(partition(my_llist, 5))


# # Sum Lists
# def sum_lists(l1, l2):
#     # function sums 2 lists which are in reverse order
#     # use a variable to store the carry over
#     carry = 0
#     l1_ptr = l1.head
#     l2_ptr = l2.head
#     sum_list = LinkedList()
#     while l1_ptr and l2_ptr:
#         l1_val = l1_ptr.data
#         l2_val = l2_ptr.data
#         # add sum modulo 10 to sum_list
#         sum_list.add_node((l1_val+l2_val+carry)%10)
#         # update carry with remainder of sum when divided
#         carry = (l1_val+l2_val+carry)//10
#         # shift pointers down their respective lists
#         l1_ptr = l1_ptr.next
#         l2_ptr = l2_ptr.next
#     return sum_list
        


# list_1 = LinkedList()
# list_2 = LinkedList()
# for i in (6, 1, 7):
#     list_1.add_node(i)
# for j in (2, 9, 5):
#     list_2.add_node(j)
# # should print sum of 617 + 295
# print(sum_lists(list_1, list_2))

