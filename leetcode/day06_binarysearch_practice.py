# ============================================================
#  DAY 06 — BINARY SEARCH  PRACTICE FILE
# ============================================================


# Q1. BINARY SEARCH  (LC #704)
# [-1,0,3,5,9,12], target=9  →  4
# Hint: lo=0, hi=end, mid=(lo+hi)//2, shrink range each step

def binary_search(nums, target):
    pass


# Q2. SEARCH INSERT POSITION  (LC #35)
# [1,3,5,6], target=2  →  1
# Hint: same as binary search; when not found, lo = insert position

def search_insert(nums, target):
    pass


# Q3. FIND MINIMUM IN ROTATED SORTED ARRAY  (LC #153)
# [3,4,5,1,2]  →  1
# Hint: if nums[mid] > nums[hi], min is in right half

def find_min(nums):
    pass


# Q4. SEARCH IN ROTATED SORTED ARRAY  (LC #33)
# [4,5,6,7,0,1,2], target=0  →  4
# Hint: one half is always sorted — check which, then decide which side

def search_rotated(nums, target):
    pass


# Q5. KOKO EATING BANANAS  (LC #875)
# piles=[3,6,7,11], h=8  →  4
# Hint: binary search on k (1 to max), check if hours <= h

def min_eating_speed(piles, h):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(binary_search([-1,0,3,5,9,12], 9))         # 4
print(search_insert([1,3,5,6], 2))               # 1
print(find_min([3,4,5,1,2]))                     # 1
print(search_rotated([4,5,6,7,0,1,2], 0))        # 4
print(min_eating_speed([3,6,7,11], 8))           # 4
