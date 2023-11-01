class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:            
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None      
        else:            
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp



        

        



    
        


        

    
    


    
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = DoublyLinkedList(7)
my_linked_list.append(8)
my_linked_list.append(9)
my_linked_list.append(10)
my_linked_list.append(11)
my_linked_list.append(12)

my_linked_list.prepend(145)

my_linked_list.pop()
my_linked_list.pop_first()

my_linked_list.print()