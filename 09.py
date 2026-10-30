#LESSON 09: STRINGS
#
#Do them in order, top to bottom.
#[EASY]   should take a few minutes
#[MEDIUM] needs some thinking - normal
#         to get stuck, ask for a hint
#[HARD]   real interview-level problem
#Write a test call for every example.


#=========== PART A: WARM-UPS ===========

#W1 [EASY]: print_chars(text)
#
#Input:  text, a string
#Output: nothing to return - just PRINT
#        each character on its own line
#Rules:
# - use a for loop over the string
#Examples:
# print_chars("cat") prints:
#   c
#   a
#   t
# print_chars("") prints nothing
def print_chars(text):
    for ch in text:
        print(ch)
test = "cat"
print(print_chars(test))


#W2 [EASY]: count_letter(text, letter)
#
#Input:  text, a string; letter, a string
#        of exactly one character
#Output: an int, how many times letter
#        appears in text
#Rules:
# - use a loop and a counter
# - do not use .count()
# - "A" and "a" are DIFFERENT here
#Examples:
# count_letter("banana", "a") -> 3
# count_letter("banana", "z") -> 0
# count_letter("Anna", "a")   -> 1
def count_letters(text, letter):
    count = 0
    
    for ch in text:
        if ch == letter:
            count += 1
    return count
print(count_letters("banana", "a"))
print(count_letters("banana", 'z'))
print(count_letters("Anna", "a"))
            


#W3 [EASY]: to_upper_list(text)
#
#Input:  text, a string
#Output: a LIST with every character of
#        text in uppercase, in the same order
#Rules:
# - start with an empty list and use .append()
# - .upper() leaves non-letters as they are
#Examples:
# to_upper_list("hi!") -> ['H', 'I', '!']
# to_upper_list("a b") -> ['A', ' ', 'B']
# to_upper_list("")    -> []

def to_upper_list(text):
    parts = []
    
    for ch in text:
        parts.append(ch.upper())
    return parts
print(to_upper_list("hi!"))
print(to_upper_list("a b"))
print(to_upper_list(""))


#=========== PART B: EXERCISES ===========

#EXERCISE 1 [EASY]: count_vowels(text)
#
#Input:  text, a string (can contain
#        spaces, capitals, punctuation)
#Output: an int, how many characters
#        in text are vowels
#Rules:
# - vowels are a, e, i, o, u
# - "A" counts the same as "a"
# - spaces, punctuation and "y" are
#   NOT vowels
# - do not use .count()
#Examples:
# count_vowels("Hello World") -> 3   (e, o, o)
# count_vowels("PYTHON")      -> 1   (O)
# count_vowels("rhythm")      -> 0
# count_vowels("")            -> 0

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count

test1 = "Hello World"
test2 = "PYTHON"
test3 = "rhythm"
test4 = ""
print(count_vowels(test1))
print(count_vowels(test2))
print(count_vowels(test3))
print(count_vowels(test4))


#EXERCISE 2 [EASY]: reverse_words(sentence)
#
#Input:  sentence, a string of words
#        separated by spaces
#Output: a NEW string with the same words
#        in reverse order, separated by
#        exactly one space
#Rules:
# - the letters inside each word stay
#   the same, only the word order flips
# - use split() and " ".join()
# - you MAY use [::-1] on the list of words
# - extra spaces at the start, end or
#   between words must disappear
#   (plain .split() with no argument
#   already handles this)
#Examples:
# reverse_words("I love python")    -> "python love I"
# reverse_words("  hello   world ") -> "world hello"
# reverse_words("single")           -> "single"

def reverse_words(sentence):
    words = sentence.split()
    backwards = words[::-1]
    return " ".join(backwards)

print(reverse_words("I love python"))
print(reverse_words("  hello world"))
print(reverse_words("single"))


#EXERCISE 3 [MEDIUM]: is_anagram(s, t)
#
#Input:  s and t, two strings of lowercase
#        letters
#Output: True if t contains exactly the same
#        letters as s, each one the same
#        number of times (order does not
#        matter); otherwise False
#Rules:
# - use a dictionary to count letters
#   (like count_frequency in 06.py)
# - do not use sorted() or Counter
# - hint for a quick exit: if the lengths
#   are different, they cannot be anagrams
#Examples:
# is_anagram("listen", "silent") -> True
# is_anagram("rat", "car")       -> False   (t vs c)
# is_anagram("aab", "abb")       -> False   (same letters, different counts)
# is_anagram("ab", "abc")        -> False   (different length)

def is_anagram(s ,t):
    frequencyS = {}
    frequencyT = {}
    
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        frequencyS[s[i]] = frequencyS.get(s[i], 0) + 1
        frequencyT[t[i]] = frequencyT.get(t[i], 0) + 1
    
    return frequencyS == frequencyT
    
print(is_anagram("listen", "silent"))
print(is_anagram("rat", "car"))


#EXERCISE 4 [MEDIUM]: is_anagram_array(s, t)
#
#Exactly the same task as exercise 3, with
#the same inputs, output and examples.
#The difference is HOW you count:
# - no dictionary
# - make counts = [0] * 26
# - use ord(ch) - ord("a") to find the box
#   for each letter
#Hint: you can use ONE list for both strings:
#add 1 for the letters of s, subtract 1 for
#the letters of t. What must every box
#contain at the end if they are anagrams?

def is_anagram_array(s, t):
    if len(s) != len(t):
        return False
    
    counts = [0] * 26
    
    for ch in s:
        counts[ord(ch) - ord("a")] += 1
    for ch in t:
        counts[ord(ch) - ord("a")] -= 1
    
    for ch in counts:
        if ch != 0:
            return False
    return True

print(is_anagram_array("listen", "silent"))
print(is_anagram_array("rat", "car"))

#EXERCISE 5 [MEDIUM]: first_unique_char(s)
#
#Input:  s, a string of lowercase letters
#Output: an int, the INDEX (position) of the
#        first character that appears
#        exactly once in the whole string;
#        -1 if every character repeats
#Rules:
# - return the index, NOT the letter
# - "first" means the smallest index
# - use two loops one after the other
#   (not nested): the first loop counts,
#   the second loop finds the answer
#Examples:
# first_unique_char("leetcode")     -> 0   ("l" appears once, at index 0)
# first_unique_char("loveleetcode") -> 2   ("l" and "o" repeat; "v" at index 2 is the first unique one)
# first_unique_char("aabb")         -> -1
# first_unique_char("z")            -> 0

def first_unique_char(s):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1
print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))


#EXERCISE 6 [MEDIUM]: caesar_shift(text, k)
#
#Input:  text, a string; k, an int from 0 to 25
#Output: a NEW string in which every
#        LOWERCASE letter moves k places
#        forward in the alphabet
#Rules:
# - wrap around after z: with k = 3,
#   x -> a, y -> b, z -> c
# - anything that is not a lowercase letter
#   (spaces, digits, capitals, "!") stays
#   exactly the same
# - steps for one letter:
#     letter -> position 0-25   (ord(ch) - ord("a"))
#     add k, then % 26 to wrap
#     position -> letter        (chr(ord("a") + position))
# - build the result with a list and "".join()
#Examples:
# caesar_shift("abc xyz", 3)  -> "def abc"
# caesar_shift("hello!", 1)   -> "ifmmp!"
# caesar_shift("Hi 2u", 2)    -> "Hk 2w"   (H stays, i -> k, u -> w)
# caesar_shift("abc", 0)      -> "abc"

def caesar_shift(text, k):
    updated = []
    
    for ch in text:
        if ch.islower():
            position = ord(ch) - ord("a")
            position = (position + k) % 26
            newL = chr(ord("a") + position)
            updated.append(newL)
        else:
            updated.append(ch)
    return "".join(updated)

print(caesar_shift("abc xyz", 3))
print(caesar_shift("hello!", 1))
            


#EXERCISE 7 [HARD]: compress(s)
#
#Input:  s, a string
#Output: a NEW string in which each group of
#        the same character in a row is
#        written as that character followed
#        by how many times it repeats
#Rules:
# - write the count even when it is 1
# - only characters NEXT TO each other form
#   a group: "aba" is three groups
# - collect the pieces in a list and return
#   "".join(list) at the end; do not use
#   result += ... on a string
# - the count is an int, so turn it into a
#   string with str(count) before adding it
#   to the list
# - remember the LAST group: after the loop
#   ends, it has not been added yet
#Examples:
# compress("aaabccdd") -> "a3b1c2d2"
# compress("aba")      -> "a1b1a1"
# compress("zzzz")     -> "z4"
# compress("")         -> ""

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
print(compress("aaabccdd"))
print(compress("aabba"))


#EXERCISE 8 [HARD]: is_clean_palindrome(text)
#
#Input:  text, a string
#Output: True or False
#A palindrome reads the same forwards and
#backwards. Here you must:
# - IGNORE every character that is not a
#   letter or a digit (spaces, commas,
#   colons...); use .isalnum()
# - treat "A" and "a" as equal; use .lower()
#   on the two characters you compare
#Rules:
# - use two pointers, left and right, like
#   is_palindrome in 08.py
# - do NOT create a cleaned-up copy of the
#   string; when a pointer is on a character
#   that is not a letter or digit, just
#   move that pointer past it
#Examples:
# is_clean_palindrome("A man, a plan, a canal: Panama") -> True
#     (only letters: amanaplanacanalpanama)
# is_clean_palindrome("race a car") -> False
#     (only letters: raceacar)
# is_clean_palindrome(" ")          -> True
#     (nothing left to compare)
# is_clean_palindrome("0P")         -> False
#     ("0" and "p" are different)

def is_clean_palindrome(text):
    left = 0
    right = len(text) - 1
    
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
            
        while left < right and not text[right].isalnum():
            right -= 1
            
        if text[left].lower() != text[right].lower():
            return False
        
        left += 1
        right -= 1
    return True

print(is_clean_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_clean_palindrome("race a car"))                       # False
print(is_clean_palindrome(" "))                                # True
print(is_clean_palindrome("0P"))                               # False
