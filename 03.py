#Given nums = [-5, 0, 8, -2, 11], 
#print 'Positive', 'Negative', or
#'Zero' for each element. 
#Use if, elif and else.

numbers = [-5, 0, 8, -2, 11]

for num in numbers:
    if num > 0:
       print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

#Print all integers from 1 to 100
#that are divisible by both 3 and 5. 
#Use a loop and the and operator.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#Given nums = [18, 4, 27, -3, 9], 
#find the smallest 
#number without using min() or sort().

nums = [18, 4, 27, -3, 9]

smallest = nums[0]

for num in nums:
    if smallest > num:
        smallest = num

print(smallest)

#Given nums = [6, 10, 14, 22, 30] and 
#target = 22, use a Boolean variable 
#named found to determine whether the 
#target exists. Print the result.

text = [6, 10, 14, 22, 30]

target = 22
found = False

for n in text:
    if n == target:
        found = True
        break
print(found)

#Given nums = [3, 12, 18, 25, 7, 15, 30],
#count how many values are 
#between 10 and 20 inclusive.

t = [3, 12, 18, 25, 7, 15, 30]
count = 0

for num in t:
    if num >= 10 and num<= 20:
        count += 1

print(count)

#Given nums = [4, 7, 2, -1, 9], 
#use a loop and a Boolean variable 
#to determine whether every number is 
#greater than zero. Stop early 
#if you find a non-positive value.

k = [4, 7, 2, -1, 9]
allPos = True

for nums in k:
    if nums <= 0:
        allPos = False
        break
print(allPos)

#determine whether the list 
#contains at least one odd number.

one = [2, 4, 6, 7, 8]

containsOdd = False

for j in one:
    if j % 2 == 1:
        containsOdd = True
        break

print(containsOdd)

#determine whether 
#every number is even.

two = [2, 4, 6, 8, 10]

isEven = True

for w in two:
    if w % 2 == 1:
        isEven = False
        break
print(isEven)
