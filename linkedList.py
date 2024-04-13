class LinkedList:
    def __init__(self, item):
        self.items = item
        self.head = None
        self.next = None

    def inserting_element_front(self, new_data):
        new_node = LinkedList(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        last = self.head
        while last != None:
            print(last.items, end=' ')
            last = last.next


# object creation

object_linkedList = LinkedList("a")
object_linkedList.inserting_element_front(98)

# inserting values
first = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)

# connecting all the values
object_linkedList.head = first
first.next = second
second.next = third
object_linkedList.print_linked_list()


#while object_linkedList.head is not None:
    #print(object_linkedList.head.items, end=" ")
    #object_linkedList.head = object_linkedList.head.next
