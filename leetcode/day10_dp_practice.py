# ============================================================
#  DAY 10 — DYNAMIC PROGRAMMING  PRACTICE FILE
# ============================================================


# Q1. CLIMBING STAIRS  (LC #70)
# n=5  →  8
# Hint: dp[i] = dp[i-1] + dp[i-2], use two variables (space O(1))

def climb_stairs(n):
    pass


# Q2. HOUSE ROBBER  (LC #198)
# [2,7,9,3,1]  →  12
# Hint: curr = max(prev1, prev2 + num), update prev2=prev1, prev1=curr

def rob(nums):
    pass


# Q3. COIN CHANGE  (LC #322)
# coins=[1,5,6,9], amount=11  →  2
# Hint: dp[0]=0, dp[i] = min(dp[i], dp[i-coin]+1) for each coin

def coin_change(coins, amount):
    pass


# Q4. LONGEST COMMON SUBSEQUENCE  (LC #1143)
# "abcde", "ace"  →  3
# Hint: 2D dp table, match→1+dp[i-1][j-1], no match→max(up, left)

def longest_common_subsequence(text1, text2):
    pass


# Q5. 0/1 KNAPSACK  (Classic)
# weights=[1,3,4,5], values=[1,4,5,7], W=7  →  9
# Hint: dp[i][w] = max(skip item i, take item i if it fits)

def knapsack(weights, values, W):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(climb_stairs(5))                                  # 8
print(rob([2, 7, 9, 3, 1]))                            # 12
print(coin_change([1, 5, 6, 9], 11))                   # 2
print(longest_common_subsequence("abcde", "ace"))       # 3
print(knapsack([1,3,4,5], [1,4,5,7], 7))               # 9
