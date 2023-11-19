class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        

    
def sort_stack(stack):
    additional_stack = Stack()

    while not stack.is_empty():       
        temp = my_stack.pop()

        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            my_stack.push(additional_stack.pop())
            print('add stack peak: ',  additional_stack.peek())        
        additional_stack.push(temp) 

    while not additional_stack.is_empty():
        my_stack.push(additional_stack.pop())
      

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()
