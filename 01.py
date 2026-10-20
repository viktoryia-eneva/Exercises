# Create a list with five numbers and print the first and last elements.

numbers = [5, 31, 2, 13, 9]

print(numbers[0])
print(numbers[-1])
print("End of problem")

# Write a loop that prints every element of your list.

for i in range(len(numbers)):
    print(numbers[i])

print("End of problem")

# Write a program that counts how many numbers in your list are greater than 10

count = 0 

for i in range(len(numbers)):
    if numbers[i] > 10:
        count += 1

print("The count is: ", count)