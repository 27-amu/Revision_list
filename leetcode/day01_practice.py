# ============================================================
#  DAY 01 — PRACTICE FILE  (Write your solutions here!)
# ============================================================


# Q1. TWO SUM  (LC #1)
# nums = [2, 7, 11, 15], target = 9  →  [0, 1]

def two_sum(nums, target):
    seen = {}
    for i , x in enumerate(nums):
        comp = target - x
        if comp in seen:
            return[seen[comp], i]
        seen[x] = i



# Q2. VALID PARENTHESES  (LC #20)
# "()[]{}"  →  True  |  "(]"  →  False

def is_valid(s):
    pass


# Q3. BEST TIME TO BUY AND SELL STOCK  (LC #121)
# [7, 1, 5, 3, 6, 4]  →  5

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit



# Q4. MAXIMUM SUBARRAY  (LC #53)  — Kadane's
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]  →  6

def max_subarray(nums):
    pass


# Q5. CONTAINS DUPLICATE  (LC #217)
# [1, 2, 3, 1]  →  True  |  [1, 2, 3, 4]  →  False

def contains_duplicate(nums):
    #return len(set(nums)) > len(nums)
    seen = set()
    for num in nums: 
        if num in seen:
             return True
        seen.add(num)
    return False


# ── TEST YOUR CODE ──────────────────────────────────────────
print(two_sum([2, 7, 11, 15], 9))          # [0, 1]
print(is_valid("()[]{}"))                   # True
print(max_profit([7, 1, 5, 3, 6, 4]))      # 5
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(contains_duplicate([1, 2, 3, 1]))    # True
