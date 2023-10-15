
class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


class LinkedList:
    def __init__(self, value): #creates new node
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1



    


    # def append(self, value): #create new node and add it to end
    # def prepend(self, value): # create new node and add it to beginning
    # def insert(self, index, value): #create new node and insert it

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)



