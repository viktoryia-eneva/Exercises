#Given nums = [1, 2, 2, 3, 4, 4, 5],
#write a function unique_values(nums)
#that returns a set containing 
#the unique numbers
#Use a loop and .add().

def unique_values(nums):
    mySet = set()
    
    for num in nums:
        mySet.add(num)
        
    return mySet

test = [1, 2, 2, 3, 4, 4, 5]
print(unique_values(test))

#Write contains_value(nums, target) 
#that creates a set from nums and 
#returns True if target exists, 
#otherwise False. 
#Test with [4, 8, 12, 16] 
#and targets 12 and 7.

def contains_value(nums, target):
    mySet = set()
    
    for num in nums:
        mySet.add(num)
        if target in mySet:
            return True
    return False

test = [4, 8, 12, 16]
t1 = 12
t2 = 7

print(contains_value(test, t1))
print(contains_value(test, t2))

#Write a function count_frequency(nums)
#that returns a dictionary with the 
#number of occurrences of each value. 
#Test with [1, 2, 2, 3, 3, 3].

def count_frequency(nums):
    frequency = {}
    
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

test = [1, 2, 2, 3, 3, 3]
print(count_frequency(test))

#Write a function count_unique(nums)
#that returns the number of distinct
#elements. 
#Test with [4, 4, 7, 9, 7, 11].

def count_unique(nums):
    mySet = set()
    
    count = 0
    
    for num in nums:
        if num not in mySet:
            count += 1
            mySet.add(num)
        
    return count

test = [4, 4, 7, 9, 7, 11]
print(count_unique(test))

#Given nums = [3, 5, 3, 2, 5, 3, 8], 
#write a function most_frequent(nums)
#that returns the number appearing 
#most often. Assume the list is 
#non-empty and there is a 
#unique most frequent number. 
#Use a dictionary.

def most_frequent(nums):
    frequency = {}
    
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        
    highest_frequency = 0
    most_frequent = None
    
    for key, value in frequency.items():
        if value > highest_frequency:
            highest_frequency = value
            most_frequent = key
    
    return most_frequent

nums = [3, 5, 3, 2, 5, 3, 8]
print(most_frequent(nums))

#Rewrite has_common_element(a, b) 
#using a set instead of nested loops.
#Test with [1, 3, 5] and [2, 4, 5],
#then [1, 3] and [2, 4].

def has_common_elements(a, b):
    seen = set(a)
    
    for num in b:
        if num in seen:
            return True
    return False

te1 = [1, 3, 5]
te2 = [2, 4, 5]
t1 = [1, 3]
t2 = [2, 4]
print(has_common_elements(te1, te2))
print(has_common_elements(t1, t2))

#It should return the first
#number you encounter for a second time 
#while scanning from left to right.

def first_repeated(nums):
    mySet = set()
    
    for num in nums:
        if num not in mySet:
            mySet.add(num)
        else:
            return num
        
    return None
    
test1 = [4, 7, 2, 7, 4]
test2 = [1, 2, 3]
test3 = [5, 5, 8, 8]
print(first_repeated(test1))
print(first_repeated(test2))
print(first_repeated(test3))