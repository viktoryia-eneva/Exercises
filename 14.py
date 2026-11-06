#LESSON 14: RECURSION
#
#Every recursive function needs:
#  1. a BASE CASE   - the small input you can
#                     answer directly (no call)
#  2. a RECURSIVE CASE - call yourself on a
#                     SMALLER input, then use it
#No loops allowed in this file unless an
#exercise says so - the point is to think
#recursively.
#Under EVERY solution write:
#  # Time: O(...)  reason (count the calls)
#  # Space: O(...) reason (how deep the
#                  call stack gets)


#=========== PART A: WARM-UPS ===========

#W1 [EASY]: countdown(n)
#
#Input:  n, an int >= 0
#Output: nothing - PRINT n, n-1, ..., 1,
#        then print "Go!"
#Rules:
# - base case: n == 0 -> print "Go!"
# - recursive case: print n, then call
#   countdown(n - 1)
#Examples:
# countdown(3) prints:
#   3
#   2
#   1
#   Go!
# countdown(0) prints: Go!

def countdown(n):
    if n == 0:
        print("Go!")
        return 
    print(n)
    countdown(n - 1) 
print(countdown(3))

#W2 [EASY]: factorial(n)
#
#Input:  n, an int >= 0
#Output: n! = n * (n-1) * ... * 1
#Rules:
# - base case: factorial(0) is 1
# - recursive case: n * factorial(n - 1)
#Examples:
# factorial(0) -> 1
# factorial(1) -> 1
# factorial(5) -> 120

def factorial(n):
    if n == 0:
     return 1
    return n * factorial(n - 1)
print(factorial(5))

#W3 [EASY]: sum_to(n)
#
#Input:  n, an int >= 0
#Output: 0 + 1 + 2 + ... + n
#Rules:
# - same shape as factorial, but with +
# - decide the base case yourself
#Examples:
# sum_to(0) -> 0
# sum_to(4) -> 10
# sum_to(10) -> 55

def sum_to(n):
    if n == 0:
        return 0
    
    return n + sum_to(n - 1)
print(sum_to(4))
print(sum_to(10))
print(sum_to(0))

#=========== PART B: EXERCISES ===========

#EXERCISE 1 [EASY]: power(base, exp)
#
#Input:  base, an int; exp, an int >= 0
#Output: base to the power exp
#Rules:
# - do not use ** or pow()
# - base case: anything to the power 0 is 1
#Examples:
# power(2, 0)  -> 1
# power(2, 5)  -> 32
# power(3, 3)  -> 27

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
print(power(2, 0))
print(power(2, 5))
print(power(3, 3))

#EXERCISE 2 [MEDIUM]: sum_list(nums, i)
#
#Input:  nums, a list of ints; i, the index
#        to start from (start with 0)
#Output: the sum of nums[i], nums[i+1], ...
#Rules:
# - base case: i == len(nums) -> 0
#   (no numbers left)
# - recursive case: nums[i] + the sum from
#   i + 1
# - call it as sum_list(nums, 0)
#Examples:
# sum_list([3, 1, 4], 0) -> 8
# sum_list([], 0)        -> 0
# sum_list([5], 0)       -> 5

def sum_list(nums, i):
    if i == len(nums):
        return 0
    
    return nums[i] + sum_list(nums, i + 1)
print(sum_list([3, 1, 4], 0))
print(sum_list([], 0))
print(sum_list([5], 0))

#EXERCISE 3 [MEDIUM]: reverse_string(s)
#
#Input:  s, a string
#Output: s reversed
#Rules:
# - no [::-1], no loops
# - idea: the reverse of "abc" is
#   the reverse of "bc" + "a"
# - you may use slicing s[1:] here
#Examples:
# reverse_string("abc")   -> "cba"
# reverse_string("a")     -> "a"
# reverse_string("")      -> ""

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("abc"))
print(reverse_string("a"))
print(reverse_string(""))

#EXERCISE 4 [MEDIUM]: count_target(nums, target, i)
#
#Input:  nums, a list; target; i, the index
#        to start from (start with 0)
#Output: how many times target appears
#        from index i to the end
#Rules:
# - same shape as sum_list, but add 1 or 0
#   instead of the number itself
#Examples:
# count_target([1, 2, 1, 1], 1, 0) -> 3
# count_target([1, 2, 3], 9, 0)    -> 0
# count_target([], 5, 0)           -> 0



#EXERCISE 5 [MEDIUM]: is_palindrome_rec(s, left, right)
#
#Input:  s, a string; left and right, the two
#        ends to compare (start with 0 and
#        len(s) - 1)
#Output: True or False
#Rules:
# - your two-pointer is_palindrome from 08.py,
#   but instead of a while loop, call yourself
#   with left + 1 and right - 1
# - base case: left >= right -> True
#Examples:
# s = "racecar"; is_palindrome_rec(s, 0, len(s) - 1) -> True
# s = "hello";   is_palindrome_rec(s, 0, len(s) - 1) -> False
# s = "";        is_palindrome_rec(s, 0, len(s) - 1) -> True



#EXERCISE 6 [MEDIUM]: sum_digits(n)
#
#Input:  n, an int >= 0
#Output: the sum of its digits
#Rules:
# - n % 10 is the LAST digit:   472 % 10  -> 2
# - n // 10 drops the last digit: 472 // 10 -> 47
# - base case: a single digit (n < 10)
#Examples:
# sum_digits(472) -> 13   (4 + 7 + 2)
# sum_digits(5)   -> 5
# sum_digits(0)   -> 0



#EXERCISE 7 [HARD]: fib(n) and fib_memo(n, memo)
#
#Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
#each number is the sum of the two before.
#
#7a: fib(n)
# - base cases: fib(0) = 0, fib(1) = 1
# - recursive case: fib(n - 1) + fib(n - 2)
# - try fib(35) and notice how slow it is
#
#7b: fib_memo(n, memo)
# - same, but remember answers in a dict
#   memo = {} so each n is worked out ONCE
#   (see the lesson)
# - call it as fib_memo(n, {})
# - fib_memo(35, {}) should be instant
#
#Examples (both versions):
# fib(0)  -> 0
# fib(1)  -> 1
# fib(10) -> 55
#Write Time and Space for BOTH versions.
#LeetCode 509; 7b is your first taste of
#dynamic programming (LeetCode 70 is the
#same idea - on NeetCode 150).
