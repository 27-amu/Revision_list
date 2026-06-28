# ============================================================
#  DAY 10 — DYNAMIC PROGRAMMING  (Asked Almost Everywhere)
#  Pattern : Break problem into subproblems, store results
#  Two styles: Top-Down (memoization) | Bottom-Up (tabulation)
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. CLIMBING STAIRS  (LC #70)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   1 or 2 steps at a time. How many ways to reach step n?
#
# Example:
#   n=2 → 2   (1+1, 2)
#   n=5 → 8
#
# Key Idea (Bottom-Up DP):
#   dp[i] = number of ways to reach step i
#   dp[i] = dp[i-1] + dp[i-2]   ← same as Fibonacci
#   Only need last 2 values → use two variables (space O(1))

def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

print("Q1:", climb_stairs(2))   # 2
print("Q1:", climb_stairs(5))   # 8


# ─────────────────────────────────────────────────────────────
# Q2. HOUSE ROBBER  (LC #198)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   You cannot rob two adjacent houses. Maximize money robbed.
#
# Example:
#   [1,2,3,1]  →  4   (rob house 0 + house 2)
#   [2,7,9,3,1] → 12  (rob house 0, 2, 4)
#
# Key Idea:
#   At each house: rob_it = nums[i] + prev_prev
#                  skip_it = prev
#   dp[i] = max(rob_it, skip_it)
#   Optimize space: only keep prev and prev_prev.

def rob(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)   # skip vs rob
        prev2, prev1 = prev1, curr
    return prev1

print("\nQ2:", rob([1, 2, 3, 1]))     # 4
print("Q2:", rob([2, 7, 9, 3, 1]))   # 12


# ─────────────────────────────────────────────────────────────
# Q3. COIN CHANGE  (LC #322)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given coin denominations and an amount, return the fewest coins
#   needed to make up the amount. -1 if not possible.
#
# Example:
#   coins=[1,5,6,9], amount=11  →  2   (5+6)
#   coins=[2], amount=3         →  -1
#
# Key Idea (Bottom-Up DP):
#   dp[i] = min coins needed to make amount i
#   dp[0] = 0 (base), dp[1..amount] = infinity initially
#   For each amount i and each coin c:
#     dp[i] = min(dp[i], dp[i - c] + 1)

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print("\nQ3:", coin_change([1, 5, 6, 9], 11))   # 2
print("Q3:", coin_change([2], 3))                # -1


# ─────────────────────────────────────────────────────────────
# Q4. LONGEST COMMON SUBSEQUENCE  (LC #1143)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return the length of the longest common subsequence of two strings.
#   (Subsequence = chars in order but not necessarily contiguous)
#
# Example:
#   text1="abcde", text2="ace"  →  3   ("ace")
#   text1="abc",   text2="abc"  →  3
#   text1="abc",   text2="def"  →  0
#
# Key Idea (2D DP):
#   dp[i][j] = LCS of text1[:i] and text2[:j]
#   If chars match: dp[i][j] = 1 + dp[i-1][j-1]
#   Else:          dp[i][j] = max(dp[i-1][j], dp[i][j-1])

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print("\nQ4:", longest_common_subsequence("abcde", "ace"))   # 3
print("Q4:", longest_common_subsequence("abc", "def"))       # 0


# ─────────────────────────────────────────────────────────────
# Q5. 0/1 KNAPSACK  (Classic)
# ─────────────────────────────────────────────────────────────
# Problem:
#   n items each with weight and value. Knapsack capacity = W.
#   Maximize total value without exceeding capacity.
#   Each item can be taken once (0 or 1 time).
#
# Example:
#   weights=[1,3,4,5], values=[1,4,5,7], W=7  →  9  (items 1+2: w=4, v=9)
#
# Key Idea (2D DP):
#   dp[i][w] = max value using first i items with capacity w
#   If item i fits (weight[i] <= w):
#     dp[i][w] = max(dp[i-1][w],  values[i] + dp[i-1][w - weights[i]])
#                     ↑ skip it        ↑ take it
#   Else: dp[i][w] = dp[i-1][w]   (can't take item i)

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

print("\nQ5:", knapsack([1,3,4,5], [1,4,5,7], 7))   # 9

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 10
# ============================================================
#  Q1  Climbing Stairs      → Time O(n)    Space O(1)
#  Q2  House Robber         → Time O(n)    Space O(1)
#  Q3  Coin Change          → Time O(n*m)  Space O(n)
#  Q4  LCS                  → Time O(m*n)  Space O(m*n)
#  Q5  0/1 Knapsack         → Time O(n*W)  Space O(n*W)
# ============================================================
