class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # WRITE THE _SINK_DOWN METHOD HERE #
    
    def _sink_down(self, ind):
        ind_max = ind

        while True:
            ind_left = self._left_child(ind)
            ind_right = self._right_child(ind)


        
            if ind_left < len(self.heap) and self.heap[ind_left] > self.heap[ind]:
                ind_max = ind_left

            if ind_right < len(self.heap) and self.heap[ind_right] > self.heap[ind]:
                ind_max = ind_right
            

            if ind != ind_max:
                self._swap(ind, ind_max)
                ind = ind_max
            else:
                return




        
        
    #                                  #
    #               
    #
    #                                  #
    #                                  #
    ####################################
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        # print(self.heap)
        self._sink_down(0)

        return max_value
        
        

myheap = MaxHeap()
myheap.insert(75)
myheap.insert(95)
myheap.insert(85)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""
