class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next

    def set_next(self, new_value):
        self.next = new_value

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_head(self, value):
        current_head = self.head
        new_node = Node(value)
        new_node.set_next(current_head)
        self.head = new_node


    def __repr__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.value)
            print(f"current.value = {current.value}")
            current = current.next
        nodes.append("None")
        return " -> ".join(nodes)


class Main:
    llist = LinkedList()
    llist.insert_head("a")
    llist.insert_head("b")
    llist.insert_head("c")
    print(llist)
