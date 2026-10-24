#Use nested loops to print every 
#multiplication combination of numbers
#1, 2 and 3. For example: 
#1 × 1 = 1, 1 × 2 = 2, and so on.

def multiplication(num):
    result = 1

    for i in range(len(num)):
        for j in range(len(num)):
             result *= j

    return result

nums = [1, 2, 3]
print(multiplication(nums))