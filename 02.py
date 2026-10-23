# Print every even number from 2 through 20 using range().
for i in range(2, 21):
  if(i % 2 == 0):
   print(i)

# Given numbers = [8, 3, 15, 6], print 
# each index and its corresponding 
# value using enumerate().

numbers = [8, 3, 15, 6]

for i,num in enumerate(numbers):
   print(i, num)

#Use a while loop to print 10 down to 1,
#then print 'Done!'

i = 10

while(i > 0):
  print(i)
  i -= 1

#Given numbers = [5, 8, 12, 3, 20], 
# find the first number greater than 10 
# print it, and stop searching.

number = [5, 8, 12, 3, 20];

for num in number:
  if(num > 10):
    print(num)
    break

#Given nums = [4, 7, 7, 2, 9], count 
#how many neighbouring pairs contain 
#equal values. Make sure you don't 
#access an index outside the list.

nums = [4, 7, 7, 2, 9]

count = 0

for i in range(len(nums) - 1):
  if(nums[i] == nums[i + 1]):
    count += 1

print(count)