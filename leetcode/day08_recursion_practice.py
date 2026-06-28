# ============================================================
#  DAY 08 — RECURSION  PRACTICE FILE
# ============================================================


# Q1. FIBONACCI NUMBER  (LC #509)
# fib(4)  →  3
# Hint: base case n<=1, recursive = fib(n-1)+fib(n-2), use memo dict

def fib(n, memo={}):
    pass


# Q2. POWER OF TWO  (LC #231)
# 16  →  True  |  3  →  False
# Hint: base n==1 True, n<=0 or odd False, recurse on n//2

def is_power_of_two(n):
    pass


# Q3. REVERSE STRING RECURSIVELY  (LC #344)
# ["h","e","l","l","o"]  →  ["o","l","l","e","h"]
# Hint: swap s[left] and s[right], recurse with left+1, right-1

def reverse_string(s, left=0, right=None):
    pass


# Q4. SUBSETS  (LC #78)
# [1,2,3]  →  [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
# Hint: at each index include or skip, backtrack after recursing

def subsets(nums):
    pass


# Q5. CLIMBING STAIRS  (LC #70)
# n=3  →  3   (same pattern as fibonacci)
# Hint: climb(n) = climb(n-1) + climb(n-2), base: n<=2 return n

def climb_stairs(n, memo={}):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(fib(10))                  # 55
print(is_power_of_two(16))      # True
arr = ["h","e","l","l","o"]
reverse_string(arr)
print(arr)                      # ["o","l","l","e","h"]
print(subsets([1,2,3]))         # all 8 subsets
print(climb_stairs(5))          # 8
