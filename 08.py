#Write reverse_list(numbers) 
#using two pointers. Reverse the 
#original list in place and return
#it. Do not use reverse() or slicing.

def reverse_list(numbers):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        numbers[left], numbers[right] = (
            numbers[right],
            numbers[left]
        )
        
        left += 1
        right -= 1
        
    return numbers

test = [1, 6, 2, 5, 6]
print(reverse_list(test))

#Write pair_sum(numbers, target) 
#for an already sorted list. Return 
#True if two different indices contain 
#values that add up to target, 
#otherwise False. Use two pointers.

def pair_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        total = numbers[right] + numbers[left]
        
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
            
    return False

test = [1, 2, 5, 6, 8]
target = 8
print(pair_sum(test, target))

#palindrome

def is_palindrome(text):
    left = 0
    right = len(text) - 1
    
    while left < right:
        if text[left] != text[right]:
            return False
        
        left += 1
        right -= 1
        
    return True

test1 = "racecar"
test2 = "hello"
print(is_palindrome(test1))
print(is_palindrome(test2))

#remove duplicate

def remove_duplicates(numbers):
    if not numbers:
        return 0
    
    write = 1
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write - 1]:
            numbers[write] = numbers[read]
            write += 1
            
    return write
    
numbers = [1, 1, 2, 3, 3, 4]
print(remove_duplicates(numbers))

#squares of a sorted array

def sorted_squares(numbers):
    left = 0
    right = len(numbers) - 1
    
    result = [0] * len(numbers)
    position = len(numbers) - 1
        
    while left <= right:
        left_square = numbers[left] ** 2
        right_square = numbers[right] ** 2
        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
            
        position -= 1
    return result

test = [-5, -2, 0, 3, 4]
print(sorted_squares(test))
         