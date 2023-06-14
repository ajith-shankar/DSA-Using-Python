# 1. Using List
# 2. Using deque from collections
# 3. Using LIFOqueue from queue (Multi Threaded Env)
# 4. Using our own implementation

# ***************************************************************************************

# 1. Using List

stack = []  # empty stack

stack.append(10)  # adding an ele at the end
stack.append(15)  # adding an ele at the end

stack.pop()  # removes last ele

top = stack[-1]  # peak ele of the stack

size = len(stack)  # size of the stack

# Time Complexity: O(1)
# cache friendly

# ***************************************************************************************

# 2. Using deque from collections

from collections import deque

stack1 = deque()  # object of deque (empty stack)

stack1.append(10)  # adding an ele at the last
stack1.append(30)
stack1.append(50)

stack1.pop()  # remove last ele

top1 = stack1[-1]  # peak ele of the stack

size2 = len(stack1)  # size of the stack

# Time Complexity: O(1)
# not cache friendly

# ******************************************************************************************

# 4. Using our own implementation (Using Singly Linked List)

import math


class Node:
    def __init__(self, dt):
        self.data = dt
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self, dt):
        if self.head is None:
            self.head = Node(dt)

        else:
            temp = Node(dt)
            temp.next = self.head
            self.head = temp
            self.sz = self.sz + 1

    def size(self):
        return self.sz

    def peak(self):
        # if stack is empty then return infinite number
        if self.head is None:
            return math.inf

        return self.head.data

    def pop(self):
        # if stack is empty then return infinite number
        if self.head is None:
            return math.inf

        res = self.head.data
        self.head = self.head.next
        self.sz = self.sz - 1
        return res


s = MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())


# Time Complexity: O(1)
# Space Complexity: O(N) where N is the size of the stack

