
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
    
    def append(self, value): #adds item to the end of the list
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
        return temp     
      
   
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
        temp = self.get(index-1)           
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True     

    def remove(self, index): #removes element from the LL
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length-1:
            self.pop()        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self): #reverses list
        temp = self.head #swap tail and head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast.next != None:        
            slow = slow.next
            print('slow:', slow.value)
            fast = fast.next.next
            print('fast: ',fast.value)
            print('division: ',fast.value%2)
        if fast.value%2  == 0:
            even = slow.next
            return even
        return slow

    # def reverse_between(self, start_index, end_index):
    #     temp_list = []
    #     temp = self.head

    #     for _ in range(start_index): #set the staring reverse point
    #         temp = temp.next
    #     temp_start = temp

    #     for _ in range(start_index, end_index+1): # make separate list to be reversed
    #         temp_list.append(temp.value)
    #         temp = temp.next        
    #     print('temp_finish: ',temp.value)        
    #     temp_list.reverse()
    #     print('temp List: ',temp_list)

    #     temp = temp_start
    #     print('temp start: ',temp)
    #     for i in temp_list:
    #         temp.value = i
    #         temp = temp.next

    def reverse_between(self, start_index, end_index):
        # 1. Edge Case: If list has only one node or none, exit.
        if self.length <= 1:
            return
    
        # 2. Create a dummy node to simplify head operations.
        dummy_node = Node(0)
        dummy_node.next = self.head
    
        # 3. Init 'previous_node', pointing just before reverse starts.
        previous_node = dummy_node
    
        # 4. Move 'previous_node' to its position.
        # It'll be at index 'start_index - 1' after this loop.
        for i in range(start_index):
            previous_node = previous_node.next
        print('previous node: ', previous_node.value)

        # 5. Init 'current_node' at 'start_index', start of reversal.
        current_node = previous_node.next        
        print('current node: ', current_node.value)
    
        # 6. Begin reversal:
        # Loop reverses nodes between 'start_index' and 'end_index'.
        for i in range(end_index - start_index):
            print('i:',i)
            # 6.1. 'node_to_move' is next node we want to reverse.
            node_to_move = current_node.next
            print('node to move: ', node_to_move.value)
    
            # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
            current_node.next = node_to_move.next
    
            # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
            node_to_move.next = previous_node.next
    
            # 6.4. Link 'previous_node' to 'node_to_move'.
            previous_node.next = node_to_move
    
        # 7. Update list head if 'start_index' was 0.
        self.head = dummy_node.next
                










            
                 


 
                 
    def print_list(self): #prints the whole list
        temp = self.head
        print('print')    
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('numver of elements in LL:', self.length)




my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)
my_linked_list.append(10)
# my_linked_list.pop()
# my_linked_list.pop()
my_linked_list.print_list()


my_linked_list.reverse_between(2,4)

# my_linked_list.reverse_between(1,4)

my_linked_list.print_list()


def find_kth_from_end(index):
    slow = my_linked_list.head
    fast = my_linked_list.head
    for _ in range(index):
        fast = fast.next
        if fast == None:
            return None    
    # print('fast:', fast.value)
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow.value
    # print('fast: ',fast)


print('test empty list: ', find_kth_from_end(5))
print('test k == length: ', find_kth_from_end(7))
print('test k < length: ', find_kth_from_end(3))
print('test k > length: ', find_kth_from_end(4))

# print('middle node: ',my_linked_list.find_middle_node())
# my_linked_list.prepend(125)
# my_linked_list.pop_first()
# my_linked_list.set_value(2,15)
# my_linked_list.print_list()
# my_linked_list.set_value(2,120)
# my_linked_list.insert(0,180)
# my_linked_list.get(3)
# my_linked_list.remove(3)
# my_linked_list.print_list()
# my_linked_list.reverse()
# my_linked_list.print_list()

# def check(expect, actual, message):
#     print(message)
#     print("EXPECTED:", expect)
#     print("RETURNED:", actual)
#     print("PASS" if expect == actual else "FAIL", "\n")


# linked_list = LinkedList(1)
# linked_list.append(2)
# linked_list.print_list()
# popped_node = linked_list.pop()
# check(2, popped_node.value, "Value of popped node (first pop):")
# check(1, linked_list.head.value, "Head of linked list (after first pop):")
# check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
# check(1, linked_list.length, "Length of linked list (after first pop):")
# popped_node = linked_list.pop()
# check(1, popped_node.value, "Value of popped node (second pop)
# check(None, linked_list.head, "Head of linked list (after second pop):")
# check(None, linked_list.tail, "Tail of linked list (after second pop):")
# check(0, linked_list.length, "Length of linked list (after second pop):")
# popped_node = linked_list.pop()
# check(None, popped_node, "Popped node from empty linked list (third pop):")
# check(None, linked_list.head, "Head of linked list (after third pop):")
# check(None, linked_list.tail, "Tail of linked list (after third pop):")
# check(0, linked_list.length, "Length of linked list (after third pop):")

