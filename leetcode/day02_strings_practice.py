# ============================================================
#  DAY 02 — STRINGS  PRACTICE FILE  (Write your solutions here!)
# ============================================================


# Q1. REVERSE A STRING  (LC #344)
# ["h","e","l","l","o"]  →  ["o","l","l","e","h"]
# Hint: two pointers, swap from both ends

def reverse_string(s):
    pass


# Q2. VALID ANAGRAM  (LC #242)
# "anagram", "nagaram"  →  True  |  "rat", "car"  →  False
# Hint: count frequency of chars in both strings

def is_anagram(s, t):
    pass


# Q3. VALID PALINDROME  (LC #125)
# "A man, a plan, a canal: Panama"  →  True
# Hint: clean the string first (isalnum + lower), then two pointers

def is_palindrome(s):
    pass


# Q4. LONGEST COMMON PREFIX  (LC #14)
# ["flower","flow","flight"]  →  "fl"
# Hint: take first word as prefix, shrink it until it fits every word

def longest_common_prefix(strs):
    pass


# Q5. FIRST UNIQUE CHARACTER  (LC #387)
# "leetcode"  →  0  |  "aabb"  →  -1
# Hint: two passes — count frequencies, then find first with count == 1

def first_unique_char(s):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(reverse_string(["h","e","l","l","o"]))         # ["o","l","l","e","h"]
print(is_anagram("anagram", "nagaram"))               # True
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(first_unique_char("leetcode"))                  # 0
