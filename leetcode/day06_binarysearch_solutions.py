# ============================================================
#  DAY 06 — BINARY SEARCH  (Asked Almost Everywhere)
#  Pattern : Eliminate half the search space each iteration
#  Template : lo=0, hi=n-1, mid=(lo+hi)//2
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. BINARY SEARCH  (LC #704)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given a sorted array and target, return index of target. -1 if absent.
#
# Example:
#   nums=[-1,0,3,5,9,12], target=9  →  4
#
# Key Idea:
#   lo and hi define the current search range.
#   mid = (lo + hi) // 2
#   If nums[mid] == target → found.
#   If nums[mid] < target  → target must be in right half → lo = mid + 1
#   If nums[mid] > target  → target must be in left half  → hi = mid - 1

def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print("Q1:", binary_search([-1,0,3,5,9,12], 9))    # 4
print("Q1:", binary_search([-1,0,3,5,9,12], 2))    # -1


# ─────────────────────────────────────────────────────────────
# Q2. SEARCH INSERT POSITION  (LC #35)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given a sorted array and target, return the index to insert target
#   so the array remains sorted (or return index if target already exists).
#
# Example:
#   [1,3,5,6], target=5  →  2
#   [1,3,5,6], target=2  →  1
#   [1,3,5,6], target=7  →  4
#
# Key Idea:
#   Standard binary search. When loop ends, lo is the insert position.

def search_insert(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo          # lo = correct insert position when not found

print("\nQ2:", search_insert([1,3,5,6], 5))    # 2
print("Q2:", search_insert([1,3,5,6], 2))      # 1
print("Q2:", search_insert([1,3,5,6], 7))      # 4


# ─────────────────────────────────────────────────────────────
# Q3. FIND MINIMUM IN ROTATED SORTED ARRAY  (LC #153)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Array was sorted then rotated at some pivot. Find the minimum element.
#
# Example:
#   [3,4,5,1,2]  →  1
#   [4,5,6,7,0,1,2]  →  0
#
# Key Idea:
#   The minimum is at the rotation point.
#   If nums[mid] > nums[hi]: min is in the RIGHT half → lo = mid + 1
#   Else: min is in the LEFT half (including mid) → hi = mid

def find_min(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

print("\nQ3:", find_min([3,4,5,1,2]))        # 1
print("Q3:", find_min([4,5,6,7,0,1,2]))     # 0
print("Q3:", find_min([11,13,15,17]))        # 11


# ─────────────────────────────────────────────────────────────
# Q4. SEARCH IN ROTATED SORTED ARRAY  (LC #33)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Same rotated array. Given target, return its index or -1.
#
# Example:
#   nums=[4,5,6,7,0,1,2], target=0  →  4
#   nums=[4,5,6,7,0,1,2], target=3  →  -1
#
# Key Idea:
#   One half of the array around mid is always sorted.
#   Check which half is sorted, then check if target lies in that half.
#   Narrow search to whichever side the target could be in.

def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:              # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                  # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print("\nQ4:", search_rotated([4,5,6,7,0,1,2], 0))   # 4
print("Q4:", search_rotated([4,5,6,7,0,1,2], 3))     # -1


# ─────────────────────────────────────────────────────────────
# Q5. KOKO EATING BANANAS  (LC #875)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Koko eats bananas. piles[i] is pile size. She can eat k bananas/hour.
#   She must finish all piles in h hours. Find minimum k.
#
# Example:
#   piles=[3,6,7,11], h=8  →  4
#
# Key Idea (Binary Search on Answer):
#   k ranges from 1 to max(piles).
#   Binary search on k: for a given k, compute hours needed.
#   hours = sum(ceil(pile/k) for pile in piles)
#   If hours <= h → k might be enough, try smaller → hi = mid
#   If hours > h  → k too small → lo = mid + 1

import math

def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            hi = mid          # mid works, try smaller
        else:
            lo = mid + 1      # mid too slow
    return lo

print("\nQ5:", min_eating_speed([3,6,7,11], 8))     # 4
print("Q5:", min_eating_speed([30,11,23,4,20], 5))  # 30

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 06
# ============================================================
#  Q1  Binary Search          → Time O(log n)        Space O(1)
#  Q2  Search Insert Position → Time O(log n)        Space O(1)
#  Q3  Min in Rotated Array   → Time O(log n)        Space O(1)
#  Q4  Search Rotated Array   → Time O(log n)        Space O(1)
#  Q5  Koko Eating Bananas    → Time O(n log m)      Space O(1)
# ============================================================
