#LESSON 11: REBUILD THE CORE PATTERNS ALONE
#
#Same topics as 01-08, new problems.
#No skeletons. For EVERY exercise:
#  1. write your plan in one comment line
#     BEFORE the code (# Plan: ...)
#  2. write the function + test calls
#  3. write Time and Space under it
#     (# Time: O(...)  # Space: O(...))
#If stuck for 10-15 min, ask for a hint.


#EXERCISE 1 [EASY]: sum_of_evens(nums)
#
#Input:  nums, a list of ints
#Output: an int, the sum of the even numbers
#Rules:
# - do not use sum()
# - negative even numbers count too
#Examples:
# sum_of_evens([1, 2, 3, 4])   -> 6
# sum_of_evens([-2, 5, 7])     -> -2
# sum_of_evens([1, 3])         -> 0
# sum_of_evens([])             -> 0



#EXERCISE 2 [EASY]: index_of_max(nums)
#
#Input:  nums, a list of ints
#Output: an int, the INDEX of the largest
#        value; -1 if the list is empty
#Rules:
# - do not use max() or .index()
# - if the largest value appears more than
#   once, return the FIRST index
#Examples:
# index_of_max([3, 9, 2, 9]) -> 1
# index_of_max([-5, -1, -3]) -> 1
# index_of_max([7])          -> 0
# index_of_max([])           -> -1



#EXERCISE 3 [EASY]: is_sorted(nums)
#
#Input:  nums, a list of ints
#Output: True if every value is <= the value
#        after it, otherwise False
#Rules:
# - compare neighbours (like 02.py)
# - stop as soon as you find a pair in the
#   wrong order
# - careful not to go past the last index
#Examples:
# is_sorted([1, 2, 2, 5]) -> True
# is_sorted([1, 3, 2])    -> False
# is_sorted([4])          -> True
# is_sorted([])           -> True



#EXERCISE 4 [MEDIUM]: count_pairs_with_sum(nums, target)
#
#Input:  nums, a list of ints; target, an int
#Output: an int, how many pairs of DIFFERENT
#        indices (i < j) add up to target
#Rules:
# - use nested loops (like 05.py)
# - each pair counts once: (0, 3) and (3, 0)
#   are the same pair
#Examples:
# count_pairs_with_sum([1, 2, 3, 4], 5) -> 2   (1+4, 2+3)
# count_pairs_with_sum([2, 2, 2], 4)    -> 3   (indices 0-1, 0-2, 1-2)
# count_pairs_with_sum([1, 1], 5)       -> 0



#EXERCISE 5 [MEDIUM]: contains_duplicate(nums)
#
#Input:  nums, a list of ints
#Output: True if any value appears at least
#        twice, otherwise False
#Rules:
# - use a set and ONE loop
# - stop as soon as you find a duplicate
# - must be O(n) time
#Examples:
# contains_duplicate([1, 2, 3, 1]) -> True
# contains_duplicate([1, 2, 3, 4]) -> False
# contains_duplicate([])           -> False
#LeetCode 217 - first problem on NeetCode 150.



#EXERCISE 6 [MEDIUM]: most_common_letter(text)
#
#Input:  text, a string
#Output: the letter (lowercase) that appears
#        most often
#Rules:
# - "A" and "a" count as the same letter
# - ignore everything that is not a letter
#   (spaces, digits, punctuation)
# - use a dictionary
# - you can assume there is exactly one
#   winner and at least one letter
#Examples:
# most_common_letter("Hello World")   -> "l"
# most_common_letter("Banana!")       -> "a"
# most_common_letter("a1 B b2")       -> "b"



#EXERCISE 7 [MEDIUM]: two_sum_sorted(nums, target)
#
#Input:  nums, a list of ints SORTED from
#        small to big; target, an int
#Output: a list [i, j] with the two INDEXES
#        (i < j) whose values add up to
#        target; [] if there are none
#Rules:
# - two pointers from both ends (like
#   pair_sum in 08.py), but return the
#   indexes instead of True
# - must be O(n) time, O(1) space
#Examples:
# two_sum_sorted([1, 3, 4, 6, 9], 10) -> [0, 4]   (1 + 9)
# two_sum_sorted([2, 7, 11, 15], 9)   -> [0, 1]
# two_sum_sorted([1, 2, 3], 10)       -> []
#Close to LeetCode 167 (NeetCode two pointers).



#EXERCISE 8 [MEDIUM]: move_zeros(nums)
#
#Input:  nums, a list of ints
#Output: the SAME list, with all non-zero
#        values first (in their original
#        order) and all zeros at the end
#Rules:
# - change the list in place, do not create
#   a new list
# - use a read pointer and a write pointer
#   (like remove_duplicates in 08.py)
# - hint: first copy every non-zero to the
#   write position, then fill the rest
#   with 0
#Examples:
# move_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
# move_zeros([0, 0, 1])        -> [1, 0, 0]
# move_zeros([4, 5])           -> [4, 5]
#LeetCode 283.



#EXERCISE 9 [HARD]: two_sum(nums, target)
#
#Input:  nums, a list of ints, NOT sorted;
#        target, an int
#Output: a list [i, j] with the two INDEXES
#        (i < j) whose values add up to
#        target; [] if there are none
#Rules:
# - must be O(n) time: one loop + a
#   dictionary that maps value -> index
# - read the worked example in the lesson
#   before you start
#Examples:
# two_sum([2, 7, 11, 15], 9) -> [0, 1]
# two_sum([3, 2, 4], 6)      -> [1, 2]
# two_sum([3, 3], 6)         -> [0, 1]
# two_sum([1, 2], 10)        -> []
#LeetCode 1 - the most famous interview
#problem, also on NeetCode 150.
