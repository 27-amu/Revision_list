# ============================================================
#  DAY 01 — TOP 5 LEETCODE QUESTIONS (Asked Almost Everywhere)
#  Language : Python
#  Topics   : Arrays, HashMap, Stack, Sliding Window, Kadane's
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. TWO SUM  (LC #1)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given an array of integers `nums` and a target integer,
#   return indices of the two numbers that add up to target.
#   Exactly one solution exists, you may not use same element twice.
#
# Example:
#   nums = [2, 7, 11, 15], target = 9  →  [0, 1]
#
# Brute Force: O(n²) — check every pair
# Optimal    : O(n)  — use a HashMap to store (value → index)
#
# Key Idea:
#   For each number x, check if (target - x) is already in the map.
#   If yes → we found our pair. If no → store x in map and move on.

def two_sum(nums, target):
    seen = {}                          # value → index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i

# Test
print("Q1:", two_sum([2, 7, 11, 15], 9))   # [0, 1]
print("Q1:", two_sum([3, 2, 4], 6))         # [1, 2]


# ─────────────────────────────────────────────────────────────
# Q2. VALID PARENTHESES  (LC #20)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given a string with '(', ')', '{', '}', '[', ']'
#   determine if the brackets are valid (properly opened & closed).
#
# Example:
#   "()[]{}"  →  True
#   "(]"      →  False
#   "([)]"    →  False
#
# Key Idea (Stack):
#   Push every opening bracket onto a stack.
#   When you see a closing bracket, the top of stack MUST be
#   its matching opener — otherwise it's invalid.
#   At the end the stack must be empty.

def is_valid(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in match:                        # closing bracket
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)                   # opening bracket
    return len(stack) == 0

# Test
print("\nQ2:", is_valid("()[]{}"))   # True
print("Q2:", is_valid("(]"))         # False
print("Q2:", is_valid("{[]}"))       # True


# ─────────────────────────────────────────────────────────────
# Q3. BEST TIME TO BUY AND SELL STOCK  (LC #121)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   prices[i] is the price of a stock on day i.
#   Find the maximum profit from ONE buy + ONE sell (buy before sell).
#
# Example:
#   [7, 1, 5, 3, 6, 4]  →  5   (buy at 1, sell at 6)
#   [7, 6, 4, 3, 1]     →  0   (prices only fall, no profit)
#
# Key Idea (Sliding Window / Greedy):
#   Track the minimum price seen so far (best day to buy).
#   At each step compute profit = current price - min_price.
#   Keep updating max_profit.

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price                         # found a cheaper buy day
        elif price - min_price > max_profit:
            max_profit = price - min_price            # found a better profit
    return max_profit

# Test
print("\nQ3:", max_profit([7, 1, 5, 3, 6, 4]))   # 5
print("Q3:", max_profit([7, 6, 4, 3, 1]))         # 0


# ─────────────────────────────────────────────────────────────
# Q4. MAXIMUM SUBARRAY  (LC #53)  —  Medium  (Kadane's Algorithm)
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given an integer array, find the contiguous subarray with
#   the largest sum and return its sum.
#
# Example:
#   [-2, 1, -3, 4, -1, 2, 1, -5, 4]  →  6   (subarray [4,-1,2,1])
#
# Key Idea (Kadane's Algorithm):
#   current_sum = max(current element, current_sum + current element)
#   → If adding the current element makes things worse, start fresh.
#   Track global max at every step.

def max_subarray(nums):
    current = nums[0]
    best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)   # extend or restart
        best = max(best, current)
    return best

# Test
print("\nQ4:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print("Q4:", max_subarray([1]))                                   # 1
print("Q4:", max_subarray([-1, -2, -3]))                         # -1


# ─────────────────────────────────────────────────────────────
# Q5. CONTAINS DUPLICATE  (LC #217)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given an integer array, return True if any value appears
#   at least twice, otherwise return False.
#
# Example:
#   [1, 2, 3, 1]      →  True
#   [1, 2, 3, 4]      →  False
#
# Approach 1 — Sort : O(n log n) — sort then check neighbours
# Approach 2 — Set  : O(n)       — add to set; if already there → duplicate
#
# Key Idea (HashSet):
#   A set stores only unique values.
#   If len(set(nums)) < len(nums), there's a duplicate.

def contains_duplicate(nums):
    return len(set(nums)) < len(nums)

# Slightly more educational version (early exit):
def contains_duplicate_v2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test
print("\nQ5:", contains_duplicate([1, 2, 3, 1]))    # True
print("Q5:", contains_duplicate([1, 2, 3, 4]))      # False

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 01
# ============================================================
#  Q1  Two Sum              → Time O(n)        Space O(n)
#  Q2  Valid Parentheses    → Time O(n)        Space O(n)
#  Q3  Buy & Sell Stock     → Time O(n)        Space O(1)
#  Q4  Maximum Subarray     → Time O(n)        Space O(1)
#  Q5  Contains Duplicate   → Time O(n)        Space O(n)
# ============================================================
