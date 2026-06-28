# ============================================================
#  DAY 08 — RECURSION  (Asked Almost Everywhere)
#  Pattern : Base case → Recursive case → Trust the recursion
#  Golden Rule: Define what the function RETURNS, then use it.
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. FIBONACCI NUMBER  (LC #509)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)
#
# Example:
#   fib(4)  →  3   (0,1,1,2,3)
#
# Approach 1 — Pure recursion: O(2^n) — very slow (recomputes)
# Approach 2 — Memoization:    O(n)   — cache results
#
# Key Idea:
#   Base case: n <= 1 → return n
#   Recursive: fib(n) = fib(n-1) + fib(n-2)

def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print("Q1:", fib(4))    # 3
print("Q1:", fib(10))   # 55


# ─────────────────────────────────────────────────────────────
# Q2. POWER OF TWO  (LC #231)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return True if n is a power of 2.
#
# Example:
#   1  →  True  (2^0)
#   16 →  True  (2^4)
#   3  →  False
#
# Key Idea (Recursion):
#   Base cases: n==1 → True, n<1 or n is odd → False
#   Recursive: is_power_of_two(n // 2)

def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

print("\nQ2:", is_power_of_two(16))   # True
print("Q2:", is_power_of_two(3))      # False
print("Q2:", is_power_of_two(1))      # True


# ─────────────────────────────────────────────────────────────
# Q3. REVERSE STRING RECURSIVELY  (LC #344)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Reverse a list of characters in-place using recursion.
#
# Example:
#   ["h","e","l","l","o"]  →  ["o","l","l","e","h"]
#
# Key Idea:
#   Swap first and last, then recurse on the inner subarray.
#   Base case: left >= right → stop.

def reverse_string(s, left=0, right=None):
    if right is None:
        right = len(s) - 1
    if left >= right:
        return
    s[left], s[right] = s[right], s[left]
    reverse_string(s, left + 1, right - 1)

arr = ["h","e","l","l","o"]
reverse_string(arr)
print("\nQ3:", arr)   # ["o","l","l","e","h"]


# ─────────────────────────────────────────────────────────────
# Q4. SUBSETS  (LC #78)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return all possible subsets of nums (the power set).
#
# Example:
#   [1,2,3]  →  [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
#
# Key Idea (Backtracking):
#   At each index, make a choice: include nums[i] or skip it.
#   Recurse with the next index.
#   When index reaches the end, add the current path to results.

def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(list(current))     # add snapshot of current subset
        for i in range(start, len(nums)):
            current.append(nums[i])      # choose
            backtrack(i + 1, current)    # explore
            current.pop()                # un-choose (backtrack)
    backtrack(0, [])
    return result

print("\nQ4:", subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]


# ─────────────────────────────────────────────────────────────
# Q5. CLIMBING STAIRS (Recursion + Memo)  (LC #70)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   You can climb 1 or 2 steps at a time.
#   How many distinct ways to reach the top (n steps)?
#
# Example:
#   n=2  →  2   (1+1, 2)
#   n=3  →  3   (1+1+1, 1+2, 2+1)
#
# Key Idea:
#   climb(n) = climb(n-1) + climb(n-2)   ← same as Fibonacci!
#   Base cases: n==1 → 1, n==2 → 2

def climb_stairs(n, memo={}):
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = climb_stairs(n-1, memo) + climb_stairs(n-2, memo)
    return memo[n]

print("\nQ5:", climb_stairs(2))    # 2
print("Q5:", climb_stairs(3))     # 3
print("Q5:", climb_stairs(5))     # 8

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 08
# ============================================================
#  Q1  Fibonacci (memo)      → Time O(n)     Space O(n)
#  Q2  Power of Two          → Time O(log n) Space O(log n)
#  Q3  Reverse String        → Time O(n)     Space O(n) [call stack]
#  Q4  Subsets               → Time O(2^n)   Space O(n)
#  Q5  Climbing Stairs       → Time O(n)     Space O(n)
# ============================================================
