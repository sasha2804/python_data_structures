
from unittest import removeResult
from xml.dom import IndexSizeErr


class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

class LinkedList:
    def __init__(self, value): #creates new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append_element(self, value): #adds item to the end of the list
        new_node = Node(value)
        if self.head is None:
             self.head = new_node
             self.tail = new_node
        else:   
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self): #pops one element
        if self.length == 0: #edge case
            return None
        temp = self.head
        pre = self.head        
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self): #pops first element
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None     
      
   
    def prepend(self, value): #add item to the beginning of the linked list
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:        
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index): #gives element based on given index number
        if index > self.length or index <= 0:
            return None
        temp = self.head     
        for _ in range(index-1):
            temp = temp.next        
        return temp

    def set_value(self, index, value): #sets element based on index and value
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False      

    def insert(self, index, value): #creates new node and inserts it to to the given location 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_element(value)
        if index > self.length or index <= 0:
            return False
        new_node = Node(value) 
        temp = self.get(index)           
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True     

    def remove(index): #removes element from the LL
        pass

    def reverse(): #reverses the whole list
        pass
                
    def print_list(self): #prints the whole list
        temp = self.head
        print('print')    
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('numver of elements in LL:', self.length)

my_linked_list = LinkedList(4)
my_linked_list.append_element(5)
my_linked_list.append_element(6)
my_linked_list.append_element(7)
my_linked_list.append_element(8)
my_linked_list.append_element(9)



# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.print_list()
# my_linked_list.prepend(125)
# my_linked_list.pop_first()
# my_linked_list.set_value(2,15)

my_linked_list.print_list()

# my_linked_list.set_value(2,120)
my_linked_list.insert(0,180)
# my_linked_list.get(3)
my_linked_list.print_list()



