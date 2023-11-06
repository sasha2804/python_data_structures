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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def is_palindrome(self):
        start = self.head
        end = self.tail
        for _ in range(self.length):
            if start.value != end.value:
                return False
            start = start.next
            end = end.prev            
        return True
    
    def swap_pairs(self):
        if self.length <= 1:
            return False
        if self.length%2 != 0:
            print('test: ',self.length//2)
            return False
        return True
        
    
    
        



        





my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(2)

# my_dll_1.append(1)

print(my_dll_1.is_palindrome())

print(my_dll_1.swap_pairs())

# my_dll_2 = DoublyLinkedList(1)
# my_dll_2.append(2)
# my_dll_2.append(3)


# print(my_dll_2.is_palindrome())