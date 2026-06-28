# ============================================================
#  DAY 03 — TWO POINTERS  PRACTICE FILE
# ============================================================


# Q1. TWO SUM II — SORTED ARRAY  (LC #167)
# [2, 7, 11, 15], target=9  →  [1, 2]
# Hint: left=0, right=end, move based on sum vs target

def two_sum_ii(numbers, target):
    pass


# Q2. MOVE ZEROES  (LC #283)
# [0, 1, 0, 3, 12]  →  [1, 3, 12, 0, 0]
# Hint: slow pointer places non-zero, fast pointer scans

def move_zeroes(nums):
    pass


# Q3. CONTAINER WITH MOST WATER  (LC #11)
# [1,8,6,2,5,4,8,3,7]  →  49
# Hint: area = min(heights) * width, move shorter side inward

def max_water(height):
    pass


# Q4. REMOVE DUPLICATES FROM SORTED ARRAY  (LC #26)
# [0,0,1,1,1,2,2,3,3,4]  →  5
# Hint: slow writes unique values, fast scans ahead

def remove_duplicates(nums):
    pass


# Q5. 3SUM  (LC #15)
# [-1, 0, 1, 2, -1, -4]  →  [[-1,-1,2],[-1,0,1]]
# Hint: sort first, fix i, then two pointers on rest

def three_sum(nums):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(two_sum_ii([2, 7, 11, 15], 9))              # [1, 2]
print(move_zeroes([0, 1, 0, 3, 12]))              # [1, 3, 12, 0, 0]
print(max_water([1,8,6,2,5,4,8,3,7]))             # 49
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))   # 5
print(three_sum([-1, 0, 1, 2, -1, -4]))           # [[-1,-1,2],[-1,0,1]]
