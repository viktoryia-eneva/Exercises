#LESSON 12: PYTHON TOOLKIT
#
#Shortcuts for things you already know how
#to write the long way. Read the worked
#example for each tool in the lesson first.
#Under EVERY solution write:
#  # Time: O(...)  reason
#  # Space: O(...) reason

from collections import Counter, defaultdict


#=========== PART A: WARM-UPS ===========

#W1 [EASY]: squares(nums)
#
#Input:  nums, a list of ints
#Output: a NEW list with every number squared
#Rules:
# - ONE line: return [ ... ] using a
#   list comprehension, no .append()
#Examples:
# squares([1, 2, 3]) -> [1, 4, 9]
# squares([-2, 0])   -> [4, 0]
# squares([])        -> []

def squares(nums):
    result = [num ** 2 for num in nums]
    return result
print(squares([1, 2, 3]))
print(squares([-2, 0]))
print(squares([]))


#W2 [EASY]: only_positive(nums)
#
#Input:  nums, a list of ints
#Output: a NEW list with only the numbers
#        greater than 0, in the same order
#Rules:
# - ONE line: a list comprehension with if
#Examples:
# only_positive([3, -1, 0, 5]) -> [3, 5]
# only_positive([-4, -2])      -> []

def only_positive(nums):
    result = [num for num in nums if num > 0]
    return result
print(only_positive([3, -1, 0, 5]))
print(only_positive([-4, -2]))

#W3 [EASY]: min_max(nums)
#
#Input:  nums, a non-empty list of ints
#Output: a TUPLE (smallest, largest)
#Rules:
# - you MAY use min() and max() here
# - return both with: return a, b
# - test it by UNPACKING the result:
#     low, high = min_max([4, 1, 9])
#     print(low, high)   -> 1 9
#Examples:
# min_max([4, 1, 9]) -> (1, 9)
# min_max([7])       -> (7, 7)

def min_max(nums):
    return min(nums), max(nums)
print(min_max([4, 1, 9]))
print(min_max([7]))

#=========== PART B: EXERCISES ===========

#EXERCISE 1 [EASY]: add_lists(a, b)
#
#Input:  a and b, two lists of ints with the
#        SAME length
#Output: a NEW list where each item is
#        a[i] + b[i]
#Rules:
# - use zip(), no indexes
# - one-line comprehension is allowed but
#   a normal loop is fine too
#Examples:
# add_lists([1, 2, 3], [10, 20, 30]) -> [11, 22, 33]
# add_lists([], [])                  -> []

def add_lists(a, b):
    result = []
    
    for x, y in zip(a, b):
        result.append(x + y)
    return result
print(add_lists([1, 2, 3], [10, 20, 30]))
print(add_lists([], []))

#EXERCISE 2 [EASY]: count_same_position(s, t)
#
#Input:  s and t, two strings, SAME length
#Output: an int, how many positions have the
#        same character in both strings
#Rules:
# - use zip()
#Examples:
# count_same_position("abcd", "abxd") -> 3
# count_same_position("abc", "xyz")   -> 0
# count_same_position("", "")         -> 0

def count_same_positions(s, t):
    count = 0
    
    for x, y in zip(s, t):
        if x == y:
          count += 1
    return count
print(count_same_positions("abcd", "abxd"))
print(count_same_positions("abc", "xyz"))
print(count_same_positions("", ""))    

#EXERCISE 3 [MEDIUM]: sort_by_length(words)
#
#Input:  words, a list of strings
#Output: a NEW list sorted from shortest to
#        longest word
#Rules:
# - use sorted() with key=len
# - words with the same length keep their
#   original order (sorted does this
#   automatically)
#Examples:
# sort_by_length(["banana", "kiwi", "fig"]) -> ["fig", "kiwi", "banana"]
# sort_by_length(["bb", "a", "cc"])         -> ["a", "bb", "cc"]

def sort_by_length(words):
    return sorted(words, key = len)
print(sort_by_length(["banana", "kiwi", "fig"]))
print(sort_by_length(["bb", "a", "cc"]))


#EXERCISE 4 [MEDIUM]: rank_students(students)
#
#Input:  students, a list of (name, score)
#        tuples
#Output: a list of NAMES only, from highest
#        score to lowest
#Rules:
# - sorted() with key=lambda and reverse=True
# - then a comprehension to keep only names
#Examples:
# rank_students([("ana", 70), ("ben", 95), ("cy", 80)])
#     -> ["ben", "cy", "ana"]
# rank_students([]) -> []

def rank_students(students):
    names = []
    
    ranked = sorted(students, key = lambda p: p[1], reverse = True)
    for name in ranked:
        names.append(name[0])
    return names
print(rank_students([("ana", 70), ("ben", 95), ("cy", 80)]))
print(rank_students([]))

#EXERCISE 5 [MEDIUM]: Counter rewrites
#
#Rewrite two functions you already wrote,
#this time with Counter.
#
#5a: is_anagram(s, t)  - ONE line
#  is_anagram("listen", "silent") -> True
#  is_anagram("aab", "abb")       -> False
#
#5b: most_frequent(nums) - use
#    Counter(...).most_common(1)
#    careful: it returns a LIST of TUPLES,
#    you must dig out just the number
#  most_frequent([3, 5, 3, 2, 3]) -> 3

def is_anagram(s, t):
    return Counter(s) == Counter(t)
print(is_anagram("listen", "silent"))
print(is_anagram("aab", "abb"))

def most_frequent(nums):
    return Counter(nums).most_common(1)[0][0]
print(most_frequent([3, 5, 3, 2, 3]))

#EXERCISE 6 [MEDIUM]: group_by_length(words)
#
#Input:  words, a list of strings
#Output: a dictionary: length -> list of the
#        words with that length (in the
#        order they appear)
#Rules:
# - use defaultdict(list), no "if key in"
#   checks
# - return dict(groups) so it prints like a
#   normal dictionary
#Examples:
# group_by_length(["cat", "dog", "hello", "hi"])
#     -> {3: ["cat", "dog"], 5: ["hello"], 2: ["hi"]}
# group_by_length([]) -> {}

def group_by_length(words):
    groups = defaultdict(list)
    
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)
print(group_by_length(["cat", "dog", "hello", "hi"]))
print(group_by_length([]))

#EXERCISE 7 [MEDIUM]: top_k_frequent(nums, k)
#
#Input:  nums, a list of ints; k, an int
#Output: a list of the k values that appear
#        MOST often (any order is fine)
#Rules:
# - count with Counter
# - then sort the KEYS by their count,
#   highest first: sorted(..., key=..., reverse=True)
# - return the first k with slicing
#Examples:
# top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
# top_k_frequent([4], 1)                -> [4]
#LeetCode 347 - on NeetCode 150.

def top_k_frequent(nums, k):
    counts = Counter(nums)
    ranked = sorted(counts, key = lambda p: counts[p], reverse = True)
    return ranked[:k]
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([4], 1))

#EXERCISE 8 [HARD]: group_anagrams(words)
#
#Input:  words, a list of lowercase strings
#Output: a list of groups; each group is a
#        list of words that are anagrams of
#        each other (any order is fine)
#Rules:
# - like exercise 6, but the KEY is the
#   word's letters sorted:
#     "".join(sorted("eat")) -> "aet"
#   all anagrams give the same key
# - defaultdict(list), then return
#   list(groups.values())
#Examples:
# group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#     -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# group_anagrams([""]) -> [[""]]
#LeetCode 49 - on NeetCode 150.

def group_anagrams(words):
    group = defaultdict(list)
    
    for word in words:
        key = "".join(sorted(word))
        group[key].append(word)
    return list(group.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))