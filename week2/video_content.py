import numpy as np
import math

# Memoization

""" def memo_test():
    cache = {}

    def closure(n):
        if n in cache:
            print("Fetching from Cache")
            return cache[n]
        else:
            print("Calculating process...")
            np.random.seed(42)
            a = np.random.rand(n,n)
            b = np.random.rand(n,n)
            c = np.dot(a,b)
            cache[n] = c
            return c
        
    return closure

if __name__ == "__main__":

    N = input("Enter the size of the matrix: ")
    N = int(N)

    matrix_calculation = memo_test()
    m1 = matrix_calculation(N)
    print(m1)

    N = input("Enter the size of the matrix: ")
    N = int(N)
    m2 = matrix_calculation(N)
    print(m2)

    N = input("Enter the size of the matrix: ")
    N = int(N)
    m3 = matrix_calculation(N)
    print(m3)   

    N = input("Enter the size of the matrix: ")
    N = int(N)
    m4 = matrix_calculation(N)
    print(m4)    """

## 4 OOP and basic data structures

""" def binary_search(arr, target):
    lo = 0
    hi = len(arr)
    
    while lo < hi: 
        m = math.floor(lo+(hi-lo)/3)
        v = arr[m]
        
        if v == target:
            return True
        if v > target:
            hi = m
        else: 
            lo = m + 1
    return False

arr = [1,2,3,4,5,6,7,8,9,10,12,32,36,64,78,78,98]

res = binary_search(arr,100)
print(res) """

 ## Pointers
 
 
class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def createNode(self, newValue):
        newNode = Node(newValue)
        newNode.left = None
        newNode.right = None
        
        return newNode
    
    def printTree(self, root): 
        if root is None: 
            return
        
        print(root.value)
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == "__main__":
    tree1 = BinaryTree()
    root1 = tree1.createNode(5)
    root1.left = tree1.createNode(3)
    root1.left.left = tree1.createNode(12)
    root1.left.right = tree1.createNode(4)
    root1.right = tree1.createNode(6)
    root1.right.right = tree1.createNode(8)
    
    tree1.printTree(root1)
    
    
        

        

