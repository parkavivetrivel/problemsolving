class LinkedList:
    def __init__(self, item):
        self.items = item
        self.head = None
        self.next = None


# object creation

object_linkedList = LinkedList("a")

# inserting values
first = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)


# connecting all the values
object_linkedList.head = first
first.next = second
second.next = third


while object_linkedList.head != None:
    print(object_linkedList.head.items, end=" ")
    object_linkedList.head = object_linkedList.head.next

