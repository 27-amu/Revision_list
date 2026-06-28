# ============================================================
#  DAY 04 — SLIDING WINDOW  PRACTICE FILE
# ============================================================


# Q1. MAXIMUM AVERAGE SUBARRAY I  (LC #643)
# [1,12,-5,-6,50,3], k=4  →  12.75
# Hint: fixed window of size k, slide it (add right, remove left)

def find_max_average(nums, k):
    pass


# Q2. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS  (LC #3)
# "abcabcbb"  →  3
# Hint: variable window + set, shrink from left when duplicate found

def length_of_longest_substring(s):
    pass


# Q3. MINIMUM SIZE SUBARRAY SUM  (LC #209)
# target=7, [2,3,1,2,4,3]  →  2
# Hint: grow window until sum>=target, then shrink and record min length

def min_subarray_len(target, nums):
    pass


# Q4. PERMUTATION IN STRING  (LC #567)
# s1="ab", s2="eidbaooo"  →  True
# Hint: fixed window of size len(s1), compare frequency arrays

def check_inclusion(s1, s2):
    pass


# Q5. LONGEST REPEATING CHARACTER REPLACEMENT  (LC #424)
# "ABAB", k=2  →  4
# Hint: valid window = window_size - max_freq_char <= k

def character_replacement(s, k):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(find_max_average([1,12,-5,-6,50,3], 4))       # 12.75
print(length_of_longest_substring("abcabcbb"))       # 3
print(min_subarray_len(7, [2,3,1,2,4,3]))            # 2
print(check_inclusion("ab", "eidbaooo"))             # True
print(character_replacement("ABAB", 2))              # 4
