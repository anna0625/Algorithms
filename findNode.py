# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Creating a single node
#first = Node(3)
#print(first.value)

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the "end" of linked list
    def insert_end(self, value):
        newNode = Node(value)
        if self.head:
            current = self.head
            # I guess it adds newNode to the end of list
            # because his while loop
            while current.next != None:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
         current = self.head
         nodes = []
         while current != None:
             nodes.append(current.value)
             current = current.next
         nodes.append("Null")
         print(" -> ".join(nodes))


class Main:
    # Linked List with a single node
    LL = LinkedList()
    #LL.head = Node(3)
    #print(LL.head.value)

    LL.insert_end("3")
    LL.insert_end("4")
    LL.insert_end("5")
    LL.printLL()
