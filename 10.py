#LESSON 10: BIG-O
#
#Most exercises here are READING code, not
#writing it. For each one, fill in:
#  Time:  O(...)
#  Space: O(...)   (only where asked)
#  Why:   one sentence in your own words
#The "Why" is the important part - in an
#interview you must explain it out loud.
#
#n = len(nums) (or len(text)), unless
#the exercise says otherwise.


#=========== PART A: WARM-UPS ===========

#W1 [EASY]

def get_first(nums):
    return nums[0]

#Time: O(___)
#Why:



#W2 [EASY]

def total(nums):
    result = 0
    for num in nums:
        result += num
    return result

#Time: O(___)
#Why:



#W3 [EASY]

def print_pairs(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(nums[i], nums[j])

#Time: O(___)
#Why:



#=========== PART B: EXERCISES ===========

#EXERCISE 1 [EASY]
#Two loops, one AFTER the other.

def min_and_max(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return smallest, largest

#Time: O(___)
#Why:



#EXERCISE 2 [MEDIUM]
#Two DIFFERENT lists: n = len(a), m = len(b).

def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False

#Time: O(___)
#Why:



#EXERCISE 3 [MEDIUM]
#Watch out for the hidden loop.

def count_shared(a, b):
    count = 0
    for x in a:
        if x in b:          #b is a LIST
            count += 1
    return count

#Time: O(___)   (n = len(a), m = len(b))
#Why:

#Now the same function, but b is turned
#into a set first. What changes?

def count_shared_fast(a, b):
    seen = set(b)
    count = 0
    for x in a:
        if x in seen:       #seen is a SET
            count += 1
    return count

#Time: O(___)
#Why:



#EXERCISE 4 [MEDIUM]
#Your compress from 09.py. It has a while
#inside a while - is it O(n^2)?

def compress(s):
    parts = []
    left = 0

    while left < len(s):
        right = left + 1
        while right < len(s) and s[right] == s[left]:
            right += 1

        parts.append(s[left] + str(right - left))
        left = right
    return "".join(parts)

#Time: O(___)
#Why:



#EXERCISE 5 [MEDIUM]
#i doubles every round instead of +1.

def count_doublings(n):
    steps = 0
    i = 1
    while i < n:
        i = i * 2
        steps += 1
    return steps

#Hint: write down i for n = 16:
#1, 2, 4, 8, 16 -> how many rounds?
#And for n = 1024?
#Time: O(___)
#Why:



#EXERCISE 6 [MEDIUM]
#SPACE this time: how much EXTRA memory
#does each function create?

def reverse_in_place(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

#Space: O(___)
#Why:

def doubled(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

#Space: O(___)
#Why:

def count_letters(text):
    counts = [0] * 26
    for ch in text:
        counts[ord(ch) - ord("a")] += 1
    return counts

#Space: O(___)   (careful: does 26 grow with text?)
#Why:



#EXERCISE 7 [HARD]: contains_duplicate(nums)
#This one you WRITE - twice.
#
#Input:  nums, a list of ints
#Output: True if any value appears at least
#        twice, False if all are different
#
#Version 1: contains_duplicate_slow(nums)
# - use nested loops (like 05.py)
# - write its Time and Space below it
#
#Version 2: contains_duplicate(nums)
# - use a set and ONE loop (like
#   first_repeated in 06.py)
# - write its Time and Space below it
#
#Examples (for both versions):
# [1, 2, 3, 1] -> True
# [1, 2, 3, 4] -> False
# []           -> False
#
#This is LeetCode 217 - the very first
#problem on the NeetCode 150 list.
