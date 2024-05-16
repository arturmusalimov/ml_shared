#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

def twoSum(nums, target):
    #we use a hash map to track on the observed numbers(this will be the keys) and set the index as a value
    res = {}

    for x, num in enumerate(nums):
        value = target - num
        if value in res:
            return [res[value], x]
        res[num] = x

    return res

#Time and space complexity: Time is O(n), we visit each number 1 time linearly, space is also O(n), since in the worst case we allocate N amount
#of elements in memory.

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):

    smallestWord = getSmallestWord(arr)
    mostCommonSet = set(smallestWord)
    for word in arr:
        findMostCommon(word, mostCommonSet)

    return list(mostCommonSet)

def getSmallestWord(words):
    smallest = words[0]

    for word in words[1:]:
        if len(word) < len(smallest):
            smallest = word

    return smallest

def findMostCommon(word, mostCommonSet):
    wordSet = set(word)
    for char in list(mostCommonSet):
        if char not in wordSet:
            mostCommonSet.remove(char)


#Time and space complexity: Time O(n.m), where M is the length of the longest word, space is O(m)

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [0, 2, 3]

def threeSum(nums):
    #we sort the array in place and use the 3 pointer technique
    nums.sort()
    target = 0
    res = []

    for i in range(len(nums)-2): #we know we're looking for 3 values, so we adjust for that window at the end N-2
        left = i +1
        right = len(nums) -1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                res.append([nums[i], nums[left], nums[right]]) #we found the 3 numbers
                left += 1
                right -= 1
                #we keep updating the pointers in case there are more combinations that will add up to 0
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1

    return res


#Time and space complexity: since we are sorting the array on avg time will be O(n log n) and space is O(1) since we know the resulting array is
#of length 3

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

def reverseList(head):
    #we need extra pointers to reference previous
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to this node
        current = next_node       # Move to next node
    return prev  # New head of the reversed list

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail

#Time and space complexity: time O(n) space O(1), we don't use extra memory



#test area

#question 1
arr = [2,3,4,2,7]
target = 10

q1 = twoSum(arr, target)
print(q1)

print("-----------------------------")

#question 2

#Example: ["flower","flow","flight"] output = "fl"
words =  ["flower","flow","flight"]

q2 = findMostCommonPrefix(words)
print(q2)

print("-----------------------------")

#question 3
#example: [1, 2, -2, -1, 3] output = [0, 2, 3]

q3_nums = [1,2,-2,-1,3]
q3 =  threeSum(q3_nums)

print(q3)
print("-----------------------------")

#question 4
print("Original List")
printList(head)
reversed_head = reverseList(head)
print("Reversed List")
printList(reversed_head)
