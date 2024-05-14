#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

""" def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(i, j)
    

twoSum([2,3,6,10], 16) """
#Time and space complexity: Time: O(n*n) / Space: I don't know, maybe just the space of the array (nums) -> n?


""" def twoSumHash(nums, target):
    global hashmap
    hashmap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i    
    return

print(twoSumHash([2,3,4,5], 9)) """

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):
    #your code goes here
    pass

#Time and space complexity:

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [0, 2, 3]

def threeSum(nums):
    #your code goes here
    pass

#Time and space complexity:

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

""" class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None

printList(head)

def reverseList(head):
    #your code goes here
    pass

#Time and space complexity: """




