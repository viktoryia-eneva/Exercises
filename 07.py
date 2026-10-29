#Write a function find_min_max(numbers)
#that returns both the smallest and
#largest numbers using just one pass. 
#Return None if the list is empty.

def find_max_min(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    
    for num in numbers:
        if not numbers:
            return None
        
        if largest < num:
            largest = num
            
        if smallest > num:
            smallest = num
    
    return largest, smallest

numbers = [8, 3, 12, 5, 1]
print(find_max_min(numbers))

#Write find_index(numbers, target)
#that returns the first index of the
#target, 
#or -1 if not found.

def find_index(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
        
    return -1
        
test = [7, 3, 9, 3, 5]
target = 3
print(find_index(test, target))

#Write count_frequencies(numbers) 
#that counts
#how many times each number appears.

def count_frequencies(numbers):
    frequences = {}
    
    for num in numbers:
        frequences[num] = frequences.get(num, 0) + 1
    return frequences

test = [2, 4, 2, 6, 4, 2]
print(count_frequencies(test))

#bubble sort

def bubble_sort(numbers):
    n = len(numbers)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j] , numbers[j + 1]=(
                    numbers[j + 1],
                    numbers[j]
                )
    return numbers

test = [9, 3, 7, 1, 5]
print(bubble_sort(test))

#selection sort

def selection_sort(numbers):
    n = len(numbers)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        
        numbers[i], numbers[min_index] = (
            numbers[min_index],
            numbers[i]
        )
    
    return numbers

test = [6, 2, 8, 1, 4]
print(selection_sort(test))

#should return the second
#largest distinct number in a list.

def second_largest(numbers):
    n = len(numbers)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )
    if not numbers:
        return None
    
    find = numbers[n - 1]
    
    for i in range(n - 2, -1, -1):
        if find > numbers[i]:
            return numbers[i]
        
    return None

def optimised(numbers):
    largest = None
    second = None
    
    for num in numbers:
        if largest is None:
            largest = num
        elif num > largest:
            second = largest
            largest = num
        elif num < largest and (second == None or num > second):
            second = num
    
    return second
        
            