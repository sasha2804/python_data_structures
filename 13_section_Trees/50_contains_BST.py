

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, check):
        if self.root == None:
            return False        
        temp = self.root
        while temp is not None:
            if check < temp.value:
                temp = temp.left
            elif check > temp.value:
                temp = temp.right
            else:
                return True
        return False
            



        



    ## WRITE INSERT METHOD HERE ##
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################

bst = BinarySearchTree()

print(bst.insert(1))
print(bst.insert(2))
print(bst.insert(3))
print(bst.insert(4))
print(bst.insert(5))
print(bst.insert(10))
print(bst.insert(11))
print(bst.insert(12))
print(bst.insert(13))
print(bst.insert(14))

print('contains: ', bst.contains(5))



##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################


# def check(expect, actual, message):
#     print(message)
#     print("EXPECTED:", expect)
#     print("RETURNED:", actual)
#     print("PASS" if expect == actual else "FAIL", "\n")

# print("\n----- Test: Insert to Empty Tree -----\n")
# bst = BinarySearchTree()
# result = bst.insert(5)
# check(True, result, "Insert 5, should succeed:")
# check(5, bst.root.value, "Root value after inserting 5:")
# check(None, bst.root.left, "Root's left child after inserting 5:")
# check(None, bst.root.right, "Root's right child after inserting 5:")

# print("\n----- Test: Insert to Existing Tree -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# result = bst.insert(3)
# check(True, result, "Insert 3, should succeed:")
# check(3, bst.root.left.left.value, "Root's left-left value after inserting 3:")
# check(None, bst.root.left.left.left, "Root's left-left-left child after inserting 3:")
# check(None, bst.root.left.left.right, "Root's left-left-right child after inserting 3:")

# print("\n----- Test: Insert Duplicate Value -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# result = bst.insert(5)
# check(False, result, "Insert 5 again, should fail:")
# check(None, bst.root.left.left, "Root's left-left child after inserting 5 again:")
# check(None, bst.root.left.right, "Root's left-right child after inserting 5 again:")

# print("\n----- Test: Insert Greater Than Root -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# result = bst.insert(15)
# check(True, result, "Insert 15, should succeed:")
# check(15, bst.root.right.value, "Root's right value after inserting 15:")
# check(None, bst.root.right.left, "Root's right-left child after inserting 15:")
# check(None, bst.root.right.right, "Root's right-right child after inserting 15:")

# print("\n----- Test: Insert Less Than Root -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# result = bst.insert(5)
# check(True, result, "Insert 5, should succeed:")
# check(5, bst.root.left.value, "Root's left value after inserting 5:")
# check(None, bst.root.left.left, "Root's left-left child after inserting 5:")
# check(None, bst.root.left.right, "Root's left-right child after inserting 5:")

