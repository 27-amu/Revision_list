# ============================================================
#  DAY 04 — SLIDING WINDOW  (Asked Almost Everywhere)
#  Pattern : Fixed window, Variable window with left/right
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. MAXIMUM AVERAGE SUBARRAY I  (LC #643)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Find the contiguous subarray of length k with maximum average.
#
# Example:
#   nums = [1,12,-5,-6,50,3], k = 4  →  12.75
#
# Key Idea (Fixed Window):
#   Build the first window of size k, then slide it.
#   Each slide: add new right element, remove leftmost element.
#   No need to re-sum the whole window every time → O(n).

def find_max_average(nums, k):
    window_sum = sum(nums[:k])          # first window
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]   # slide: add right, remove left
        max_sum = max(max_sum, window_sum)
    return max_sum / k

print("Q1:", find_max_average([1,12,-5,-6,50,3], 4))   # 12.75


# ─────────────────────────────────────────────────────────────
# Q2. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS  (LC #3)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Find the length of the longest substring with all unique characters.
#
# Example:
#   "abcabcbb"  →  3  ("abc")
#   "bbbbb"     →  1  ("b")
#   "pwwkew"    →  3  ("wke")
#
# Key Idea (Variable Window + HashSet):
#   Expand right pointer, adding chars to a set.
#   When a duplicate is found, shrink from the left until it's gone.
#   Track max window size throughout.

def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:          # shrink window until no duplicate
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print("\nQ2:", length_of_longest_substring("abcabcbb"))   # 3
print("Q2:", length_of_longest_substring("bbbbb"))        # 1
print("Q2:", length_of_longest_substring("pwwkew"))       # 3


# ─────────────────────────────────────────────────────────────
# Q3. MINIMUM SIZE SUBARRAY SUM  (LC #209)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Find the minimal length of a contiguous subarray whose sum >= target.
#   Return 0 if no such subarray exists.
#
# Example:
#   target=7, nums=[2,3,1,2,4,3]  →  2  (subarray [4,3])
#
# Key Idea (Variable Window):
#   Expand right to grow the window sum.
#   Once sum >= target, try to shrink from left (record min length).
#   Keep shrinking while sum still >= target.

def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

print("\nQ3:", min_subarray_len(7, [2,3,1,2,4,3]))   # 2
print("Q3:", min_subarray_len(4, [1,4,4]))            # 1


# ─────────────────────────────────────────────────────────────
# Q4. PERMUTATION IN STRING  (LC #567)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return True if s2 contains a permutation of s1 as a substring.
#
# Example:
#   s1="ab", s2="eidbaooo"  →  True   ("ba" is a permutation of "ab")
#   s1="ab", s2="eidboaoo"  →  False
#
# Key Idea (Fixed Window = len(s1), Frequency Map):
#   Keep a frequency count of s1.
#   Slide a window of size len(s1) over s2.
#   At each position compare frequency maps → O(26) = O(1).

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    count1 = [0] * 26
    count2 = [0] * 26
    for ch in s1:
        count1[ord(ch) - ord('a')] += 1
    for i in range(len(s1)):               # build first window
        count2[ord(s2[i]) - ord('a')] += 1
    if count1 == count2:
        return True
    for i in range(len(s1), len(s2)):
        count2[ord(s2[i]) - ord('a')] += 1               # add new right
        count2[ord(s2[i - len(s1)]) - ord('a')] -= 1     # remove old left
        if count1 == count2:
            return True
    return False

print("\nQ4:", check_inclusion("ab", "eidbaooo"))   # True
print("Q4:", check_inclusion("ab", "eidboaoo"))     # False


# ─────────────────────────────────────────────────────────────
# Q5. LONGEST REPEATING CHARACTER REPLACEMENT  (LC #424)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   You can replace at most k characters in the string.
#   Find the length of the longest substring with all same characters.
#
# Example:
#   s="ABAB", k=2  →  4   (replace both B's → "AAAA")
#   s="AABABBA", k=1  →  4
#
# Key Idea:
#   Window is valid if: (window_size - count_of_most_frequent_char) <= k
#   That means we need at most k replacements to make all chars the same.
#   Expand right; if window invalid, shrink from left.

def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_len = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])
        while (right - left + 1) - max_freq > k:    # need too many replacements
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print("\nQ5:", character_replacement("ABAB", 2))      # 4
print("Q5:", character_replacement("AABABBA", 1))     # 4

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 04
# ============================================================
#  Q1  Max Average Subarray      → Time O(n)   Space O(1)
#  Q2  Longest Substring No Rep  → Time O(n)   Space O(n)
#  Q3  Min Size Subarray Sum     → Time O(n)   Space O(1)
#  Q4  Permutation in String     → Time O(n)   Space O(1)
#  Q5  Char Replacement          → Time O(n)   Space O(n)
# ============================================================
