class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top

        if self.height == 1:
            self.height -= 1
            return temp

       
        
        self.height -= 1
        return temp 
    
    def print(self):
        temp  = self.top
        while temp is not None:
            print(temp.value)
            temp  = temp.next
        


stack = Stack(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print()


print('\n')

stack.pop()

stack.print()