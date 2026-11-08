#LESSON 15: CLASSES, LINKED LISTS, TREES
#
#A class is a blueprint; an object is one
#thing built from it. Read the lesson first.
#Under EVERY function or method write:
#  # Time: O(...)  reason
#  # Space: O(...) reason
#For linked lists n = number of nodes;
#for trees n = number of nodes, h = height.


#=========== PART A: WARM-UPS ===========

#W1 [EASY]: class Dog
#
# - __init__(self, name, age) stores both
# - describe(self) RETURNS the string
#   "<name> is <age> years old"
#Test:
# d = Dog("Rex", 3)
# print(d.name)        -> Rex
# print(d.describe())  -> Rex is 3 years old

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describe(self):
        return self.name + " is " + str(self.age) + " years old"
d = Dog("Rex", 3)
print(d.name)
print(d.describe())

#W2 [EASY]: class Clicker
#
# - starts at 0 (no parameters besides self)
# - click(self)  adds 1
# - get(self)    returns the current number
# - reset(self)  sets it back to 0
#Test:
# c = Clicker()
# c.click(); c.click(); c.click()
# print(c.get())   -> 3
# c.reset()
# print(c.get())   -> 0
# Two clickers must be separate:
# a = Clicker(); b = Clicker()
# a.click()
# print(a.get(), b.get())  -> 1 0

class Clicker:
    def __init__(self):
        self.count = 0
        
    def click(self):
        self.count += 1
    
    def get(self):
        return self.count
    
    def reset(self):
        self.count = 0
        
c = Clicker()
c.click(); c.click(); c.click()
print(c.get())
c.reset()
a = Clicker()
b = Clicker()
a.click()
print(a.get(), b.get())

#W3 [EASY]: class Rectangle
#
# - __init__(self, width, height)
# - area(self)       returns width * height
# - perimeter(self)  returns 2 * (width + height)
#Test:
# r = Rectangle(3, 4)
# print(r.area())       -> 12
# print(r.perimeter())  -> 14

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)
r = Rectangle(3 , 4)
print(r.area())
print(r.perimeter())
    
#=========== PART B: EXERCISES ===========

#EXERCISE 1 [EASY]: class Wallet
#
# - __init__(self) starts with balance 0
# - add(self, amount)    adds to the balance
# - spend(self, amount)  if there is enough,
#   subtract it and return True; otherwise
#   change NOTHING and return False
# - get_balance(self)    returns the balance
#Test:
# w = Wallet()
# w.add(50)
# print(w.spend(20))       -> True
# print(w.spend(100))      -> False
# print(w.get_balance())   -> 30

class Wallet:
    def __init__(self):
        

#EXERCISE 2 [MEDIUM]: class Stack
#
#A stack: the LAST item pushed is the FIRST
#one popped (like a pile of plates).
# - __init__(self)  an empty list inside
# - push(self, x)   put x on top
# - pop(self)       remove the top item and
#                   return it; None if empty
# - peek(self)      return the top item WITHOUT
#                   removing it; None if empty
# - is_empty(self)  True or False
# - size(self)      how many items
#Rules:
# - the END of the list is the top:
#   use .append() and .pop()
#Test:
# s = Stack()
# s.push(1); s.push(2); s.push(3)
# print(s.peek())      -> 3
# print(s.pop())       -> 3
# print(s.pop())       -> 2
# print(s.size())      -> 1
# print(s.is_empty())  -> False
# s.pop()
# print(s.pop())       -> None
#You will use stacks in NeetCode's Stack
#section (e.g. LeetCode 20, Valid Parentheses).



#EXERCISE 3 [MEDIUM]: class ListNode + print_list(head)
#
#3a: write class ListNode
# - __init__(self, val, next=None)
#   stores val and next
#
#3b: build the list 1 -> 2 -> 3 BY HAND
#   (three ListNode objects linked together)
#   and keep the first one in a variable head
#
#3c: print_list(head)
# - walk the list with a while loop and
#   print each val on its own line
#Test:
# print_list(head) prints:
#   1
#   2
#   3
# print_list(None) prints nothing



#EXERCISE 4 [MEDIUM]: list_length(head), list_sum(head)
#
#Input:  head, the first node (or None)
#Output: how many nodes / the sum of all vals
#Rules:
# - a while loop, like print_list
#Examples (using head from exercise 3):
# list_length(head) -> 3
# list_sum(head)    -> 6
# list_length(None) -> 0
# list_sum(None)    -> 0



#EXERCISE 5 [MEDIUM]: build_list(values), to_python_list(head)
#
#5a: build_list(values)
# - input: a normal Python list, e.g. [4, 5, 6]
# - output: the HEAD of a linked list
#   4 -> 5 -> 6 (None if values is empty)
# - hint: use a "dummy" node in front, and a
#   tail pointer you move forward (see the
#   lesson)
#
#5b: to_python_list(head)
# - the opposite: linked list -> Python list
#Test:
# h = build_list([4, 5, 6])
# print(to_python_list(h))               -> [4, 5, 6]
# print(to_python_list(build_list([])))  -> []
#These two helpers let you test every
#linked list problem in Phase 2.



#EXERCISE 6 [MEDIUM]: class TreeNode + count_nodes(root)
#
#6a: write class TreeNode
# - __init__(self, val, left=None, right=None)
#
#6b: build this tree BY HAND:
#
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#6c: count_nodes(root) - RECURSIVE
# - base case: root is None -> 0
# - otherwise: 1 + nodes on the left
#              + nodes on the right
#Test:
# print(count_nodes(root))   -> 5
# print(count_nodes(None))   -> 0



#EXERCISE 7 [HARD]: max_depth(root)
#
#Input:  root, a TreeNode (or None)
#Output: the number of nodes on the LONGEST
#        path from the root down to a leaf
#Rules:
# - recursive, same shape as count_nodes
# - base case: None has depth 0
# - my depth = 1 + the BIGGER of my left
#   depth and my right depth (use max())
#Examples (tree from exercise 6):
# max_depth(root)               -> 3   (1 -> 2 -> 4)
# max_depth(TreeNode(7))        -> 1
# max_depth(None)               -> 0
#LeetCode 104 - on NeetCode 150.
