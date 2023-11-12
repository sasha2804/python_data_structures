class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if self.first is None:
            return None        
        temp = self.first
        if self.length == 1:
            return temp        
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp

    def print(self):
        temp = self.first
        print('last: ', self.last.value)
        print('first: ', self.first.value)
        while temp is not None:
            print(temp.value)
            temp = temp.next


qu = Queue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)

qu.print()

qu.dequeue()
qu.print()