# ============================================================
#  DAY 02 — STRINGS  (Asked Almost Everywhere)
#  Pattern : String traversal, frequency count, two pointers
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. REVERSE A STRING  (LC #344)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Reverse a list of characters in-place.
#
# Example:
#   ["h","e","l","l","o"]  →  ["o","l","l","e","h"]
#
# Key Idea (Two Pointers):
#   Use a left pointer starting at 0 and right pointer at end.
#   Swap characters and move both pointers inward until they meet.

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]   # swap
        left += 1
        right -= 1
    return s

# Test
print("Q1:", reverse_string(["h","e","l","l","o"]))   # ["o","l","l","e","h"]
print("Q1:", reverse_string(["A","b","c"]))            # ["c","b","A"]


# ─────────────────────────────────────────────────────────────
# Q2. VALID ANAGRAM  (LC #242)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given two strings s and t, return True if t is an anagram of s.
#   Anagram = same letters, same frequency, different order.
#
# Example:
#   s = "anagram", t = "nagaram"  →  True
#   s = "rat",     t = "car"      →  False
#
# Key Idea (Frequency Count):
#   Count frequency of each character in both strings.
#   If counts match → anagram.
#   Shortcut: sorted(s) == sorted(t)  but that's O(n log n)
#   Better   : use a dictionary → O(n)

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1    # count up for s
    for ch in t:
        count[ch] = count.get(ch, 0) - 1    # count down for t
        if count[ch] < 0:
            return False                      # t has extra char
    return True

# Test
print("\nQ2:", is_anagram("anagram", "nagaram"))   # True
print("Q2:", is_anagram("rat", "car"))             # False


# ─────────────────────────────────────────────────────────────
# Q3. VALID PALINDROME  (LC #125)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   A phrase is a palindrome if it reads the same forward and backward
#   after keeping only alphanumeric characters and lowercasing.
#
# Example:
#   "A man, a plan, a canal: Panama"  →  True
#   "race a car"                       →  False
#
# Key Idea (Two Pointers after cleaning):
#   Step 1: Keep only letters and digits, lowercase everything.
#   Step 2: Use left & right pointers — compare and move inward.

def is_palindrome(s):
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Test
print("\nQ3:", is_palindrome("A man, a plan, a canal: Panama"))  # True
print("Q3:", is_palindrome("race a car"))                        # False


# ─────────────────────────────────────────────────────────────
# Q4. LONGEST COMMON PREFIX  (LC #14)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Find the longest common prefix string among an array of strings.
#   Return "" if there is no common prefix.
#
# Example:
#   ["flower","flow","flight"]  →  "fl"
#   ["dog","racecar","car"]     →  ""
#
# Key Idea:
#   Take the first word as the reference prefix.
#   For every other word, shrink the prefix from the right
#   until it matches the start of that word.

def longest_common_prefix(strs):
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]            # chop last character
            if not prefix:
                return ""
    return prefix

# Test
print("\nQ4:", longest_common_prefix(["flower","flow","flight"]))  # "fl"
print("Q4:", longest_common_prefix(["dog","racecar","car"]))       # ""


# ─────────────────────────────────────────────────────────────
# Q5. FIRST UNIQUE CHARACTER  (LC #387)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given a string, find the first non-repeating character
#   and return its index. Return -1 if none exists.
#
# Example:
#   "leetcode"  →  0   ('l' appears once, at index 0)
#   "loveleet"  →  2   ('v' is first unique)
#   "aabb"      →  -1
#
# Key Idea (Two-pass with HashMap):
#   Pass 1: Count frequency of every character.
#   Pass 2: Return index of first character with frequency == 1.

def first_unique_char(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1   # pass 1: build freq map
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i                         # pass 2: first unique
    return -1

# Test
print("\nQ5:", first_unique_char("leetcode"))   # 0
print("Q5:", first_unique_char("loveleet"))     # 2
print("Q5:", first_unique_char("aabb"))         # -1

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 02
# ============================================================
#  Q1  Reverse String         → Time O(n)   Space O(1)
#  Q2  Valid Anagram          → Time O(n)   Space O(n)
#  Q3  Valid Palindrome       → Time O(n)   Space O(n)
#  Q4  Longest Common Prefix  → Time O(n*m) Space O(1)
#  Q5  First Unique Char      → Time O(n)   Space O(n)
# ============================================================
