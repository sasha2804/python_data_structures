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
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length//2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp is not None:            
            temp.value = value
            return True
        return None

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.next = after
        after.prev = new_node
        before.next = new_node
        new_node.prev = before
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()            
        if index == self.length-1:
            return self.pop()        
        before = self.get(index - 1)
        rem_node = self.get(index)
        after = self.get(index + 1) 
        before.next = after
        after.prev = before
        rem_node.next = None
        rem_node.prev = None
        self.length -= 1
        return rem_node

    def swap_first_last(self):
        if self.head is None:
            return None
        a = self.head
        b = self.tail
        a.value, b.value = b.value, a.value
        return True
    
    def reverse(self):
        # a = self.head
        # b = self.tail
        # a, b = b, a
        current = self.head
        


        temp = self.head
        self.head = self.tail
        self.tail = temp

        
        
        
        
     
    

    
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
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(50)
my_linked_list.append(60)

my_linked_list.set(5, 185)

my_linked_list.insert(2, 888)

my_linked_list.print()

my_linked_list.remove(1)

# my_linked_list.swap_first_last()
# my_linked_list.swap_first_last()

my_linked_list.reverse()

print('\n')
my_linked_list.print()

# print('\n length: ',my_linked_list.length)
# print('get method: ',my_linked_list.get(5))