# ============================================================
#  DAY 03 — TWO POINTERS  (Asked Almost Everywhere)
#  Pattern : Left/Right pointers moving toward each other
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. TWO SUM II — SORTED ARRAY  (LC #167)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Array is already sorted in ascending order.
#   Find two numbers that add up to target. Return 1-indexed positions.
#
# Example:
#   numbers = [2, 7, 11, 15], target = 9  →  [1, 2]
#
# Key Idea:
#   Since array is sorted, place left=0 and right=end.
#   If sum < target → move left right (need bigger number)
#   If sum > target → move right left (need smaller number)
#   If sum == target → found!

def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]    # 1-indexed
        elif s < target:
            left += 1
        else:
            right -= 1

print("Q1:", two_sum_ii([2, 7, 11, 15], 9))    # [1, 2]
print("Q1:", two_sum_ii([2, 3, 4], 6))          # [1, 3]


# ─────────────────────────────────────────────────────────────
# Q2. MOVE ZEROES  (LC #283)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Move all 0s to the end while keeping relative order of non-zero elements.
#   Do it in-place.
#
# Example:
#   [0, 1, 0, 3, 12]  →  [1, 3, 12, 0, 0]
#
# Key Idea (Two Pointers):
#   slow pointer marks the position to place the next non-zero.
#   fast pointer scans the array.
#   Whenever fast finds a non-zero, swap with slow, then advance slow.

def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

print("\nQ2:", move_zeroes([0, 1, 0, 3, 12]))   # [1, 3, 12, 0, 0]
print("Q2:", move_zeroes([0, 0, 1]))             # [1, 0, 0]


# ─────────────────────────────────────────────────────────────
# Q3. CONTAINER WITH MOST WATER  (LC #11)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   height[i] is height of a vertical line at position i.
#   Find two lines that together with the x-axis forms a container
#   that holds the most water.
#
# Example:
#   [1,8,6,2,5,4,8,3,7]  →  49
#
# Key Idea:
#   Area = min(height[left], height[right]) * (right - left)
#   Always move the pointer with the SHORTER height inward.
#   (Moving the taller one can only decrease area.)

def max_water(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

print("\nQ3:", max_water([1,8,6,2,5,4,8,3,7]))   # 49
print("Q3:", max_water([1, 1]))                    # 1


# ─────────────────────────────────────────────────────────────
# Q4. REMOVE DUPLICATES FROM SORTED ARRAY  (LC #26)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given a sorted array, remove duplicates in-place.
#   Return the count of unique elements (k).
#   First k elements of array should hold unique values.
#
# Example:
#   [1,1,2]        →  k=2, array=[1,2,_]
#   [0,0,1,1,1,2,2,3,3,4]  →  k=5, array=[0,1,2,3,4,_,_,_,_,_]
#
# Key Idea:
#   slow pointer = position to write the next unique element.
#   fast pointer scans ahead. When it finds a new value (≠ slow),
#   write it at slow+1 and advance slow.

def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

print("\nQ4:", remove_duplicates([1, 1, 2]))               # 2
print("Q4:", remove_duplicates([0,0,1,1,1,2,2,3,3,4]))    # 5


# ─────────────────────────────────────────────────────────────
# Q5. 3SUM  (LC #15)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Find all unique triplets [nums[i], nums[j], nums[k]] such that
#   i != j != k and nums[i] + nums[j] + nums[k] == 0.
#
# Example:
#   [-1, 0, 1, 2, -1, -4]  →  [[-1,-1,2],[-1,0,1]]
#
# Key Idea:
#   Sort the array first.
#   Fix one element (i), then use two pointers on the rest.
#   Skip duplicates to avoid duplicate triplets.

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate fixed element
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result

print("\nQ5:", three_sum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]
print("Q5:", three_sum([0, 0, 0]))                  # [[0,0,0]]

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 03
# ============================================================
#  Q1  Two Sum II             → Time O(n)       Space O(1)
#  Q2  Move Zeroes            → Time O(n)       Space O(1)
#  Q3  Container With Water   → Time O(n)       Space O(1)
#  Q4  Remove Duplicates      → Time O(n)       Space O(1)
#  Q5  3Sum                   → Time O(n²)      Space O(1)
# ============================================================
