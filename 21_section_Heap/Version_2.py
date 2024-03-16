class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self, index):
        return (index - 1)//2
    
    def _child_left(self, index):
        return index*2 + 1
    
    def _chilf_right(self, index):
        return index*2 + 2

    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._child_left(index)
            right_index = self._chilf_right(index)

            if left_index < len(self.heap) and self.heap[max_index] < self.heap[left_index]:
                max_index = left_index
            
            if right_index < len(self.heap) and self.heap[max_index] < self.heap[right_index]:
                max_index = right_index
            
            if index != max_index:
                self._swap(index, max_index)
                index = max_index
            else:
                return       
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[self._parent(current)] < self.heap[current]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
            # print('cycle while')        
        print('heap: ', self.heap)
    
    def remove(self):
        if len(self.heap) == 0:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        print('heap: ', self.heap) #######
        return max_val
    
    






myheap = MaxHeap()

myheap.insert(75)
myheap.insert(61)
myheap.insert(65)
myheap.insert(72)
myheap.remove()
# myheap.insert(55)
# myheap.insert(50)
# myheap.insert(100)
# myheap.insert(100)






    


        
    
# print(5//2)