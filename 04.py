#Write a function double(num) that returns num multiplied by 2. Test it with 7 and 15.

def double(num):
    total = num * 2
    return total

print(double(7))
print(double(15))


#Write a function is_even(num) that 
#returns True if the 
#number is even and False otherwise.

def es_even(num):
    if num % 2 == 0:
        return True

    return False

n = int(input())
print(es_even(n))

#Write a function calculate_sum(nums) 
#that returns the sum of all elements 
#without using sum(). 
#Test with [4, 7, 2, 9].

def calculate_sum(nums):
    sum = 0

    for num in nums:
        sum += num

    return sum

numbers = [4, 7, 2, 9]
print(calculate_sum(numbers))

#Write a function find_max(nums) 
#that returns the largest element 
#without using max() or sort(). 
#Assume the list is non-empty. 
#Test with [12, 5, 28, 3, 19].

def find_max(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest

elements = [12, 5, 28, 3, 19]
print(find_max(elements))

#Write a function 
#contains_target(nums, target) that 
#returns True if target exists in the 
#list and False otherwise. Test it with
#[3, 8, 12, 17] 
#using targets 12 and 20.

def contains_target(nums, target):
     for num in nums:
         if num == target:
            return True
         
     return False

target = [3, 8, 12, 17]
print(contains_target(target,12))
print(contains_target(target,20))

#Write a function count_positive(nums) 
#that returns the number of positive 
#elements. 
#Test with [-3, 5, 0, 8, -2, 11].

def count_positive(nums):
    count = 0

    for num in nums:
        if num > 0:
            count += 1

    return count

test = [-3, 5, 0, 8, -2, 11]
print(count_positive(test))

#Write a function all_greater_than_five
#(nums) that returns True only when 
#every element is greater than 5. 
#Stop early when a number fails.
#Test with [7, 9, 12] and [7, 3, 12].

def all_greater_than_five(nums):
    for num in nums:
        if num <= 5:
            return False

    return True

test1 = [7, 9, 12]
test2 = [7, 3, 12]

print(all_greater_than_five(test1))
print(all_greater_than_five(test2))
