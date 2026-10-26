#Use nested loops to print every 
#multiplication combination of numbers
#1, 2 and 3. For example: 
#1 × 1 = 1, 1 × 2 = 2, and so on.

def multiplication(num):
    for i in range(len(num)):
        for j in range(len(num)):
             result = num[i] * num[j]
             print(num[i], "x", num[j], "=", result)

nums = [1, 2, 3]
multiplication(nums)

#Given nums = [5, 8, 12, 3], 
#print every pair of values 
#corresponding to indices i and j 
#where i < j. 
#Do not repeat pairs in reverse order.

def correspond(num):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            print(num[i] , num[j])
    
nums = [5, 8, 12, 3]
correspond(nums)

#Write function count_equal_pairs(nums)
#that returns how many pairs of 
#elements at 
#different indices have equal values.

def count_equal_pairs(nums):
    count = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    
    return count
    
nums = [1, 2, 1, 2, 1]
print(count_equal_pairs(nums))

#Write a function 
#has_pair_sum(nums, target) that 
#returns True if two elements at
#different indices add up to target.
#Test with 
#[2, 7, 11, 15] and targets 9 and 20.

def has_pair_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
            
    return False
        
n = [2, 7, 11, 15]
target1 = 9
target2 = 20
print(has_pair_sum(n, target1))
print(has_pair_sum(n, target2))

#Given nums = [4, 1, 6, 3], 
#count index pairs (i, j) where i < j 
#and nums[i] < nums[j].
#Return the count from a function.

def index(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i < j and nums[i] < nums[j]:
                count += 1
                
    return count

nums = [4, 1, 6, 3]
print(index(nums))

#Write function has_common_element(a, b)
#that returns True if two lists share
#at least one value. Use nested loops,
#and stop as soon as you find a match.
#Test with [1, 3, 5] and [2, 4, 5], 
#then [1, 3] and [2, 4].

def has_common_element(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return True
    return False

l1 = [1, 3, 5]
l2 = [2, 4, 5]
print(has_common_element(l1, l2))