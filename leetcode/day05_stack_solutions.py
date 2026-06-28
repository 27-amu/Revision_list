# ============================================================
#  DAY 05 — STACK & QUEUE  (Asked Almost Everywhere)
#  Pattern : LIFO stack, monotonic stack, queue simulation
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1. MIN STACK  (LC #155)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Design a stack that supports push, pop, top, and getMin in O(1).
#
# Key Idea:
#   Maintain a second "min_stack" that tracks the current minimum
#   at every level. When you push x, also push current min to min_stack.
#   When you pop, pop from both stacks.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # min is either val itself or whatever was the previous min
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

ms = MinStack()
ms.push(-2); ms.push(0); ms.push(-3)
print("Q1 getMin:", ms.getMin())   # -3
ms.pop()
print("Q1 top:", ms.top())         # 0
print("Q1 getMin:", ms.getMin())   # -2


# ─────────────────────────────────────────────────────────────
# Q2. EVALUATE REVERSE POLISH NOTATION  (LC #150)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#   Valid operators: +, -, *, /  (integer division truncated toward zero)
#
# Example:
#   ["2","1","+","3","*"]  →  9   ((2+1)*3)
#   ["4","13","5","/","+"] →  6   (4+(13/5))
#
# Key Idea:
#   Push numbers onto stack.
#   When operator is found, pop two numbers, apply operator, push result.

def eval_rpn(tokens):
    stack = []
    ops = {'+', '-', '*', '/'}
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()   # b is second operand
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            elif t == '/': stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(t))
    return stack[0]

print("\nQ2:", eval_rpn(["2","1","+","3","*"]))          # 9
print("Q2:", eval_rpn(["4","13","5","/","+"]))           # 6


# ─────────────────────────────────────────────────────────────
# Q3. DAILY TEMPERATURES  (LC #739)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given daily temperatures, return array where answer[i] is the number
#   of days until a warmer temperature. 0 if no warmer day exists.
#
# Example:
#   [73,74,75,71,69,72,76,73]  →  [1,1,4,2,1,1,0,0]
#
# Key Idea (Monotonic Decreasing Stack):
#   Stack stores indices of temperatures in decreasing order.
#   When current temp > temp at top of stack → we found its warmer day.
#   answer[top_index] = current_index - top_index

def daily_temperatures(temps):
    answer = [0] * len(temps)
    stack = []                      # stores indices
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    return answer

print("\nQ3:", daily_temperatures([73,74,75,71,69,72,76,73]))   # [1,1,4,2,1,1,0,0]


# ─────────────────────────────────────────────────────────────
# Q4. IMPLEMENT QUEUE USING STACKS  (LC #232)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Implement a FIFO queue using only two stacks.
#   Supports: push, pop, peek, empty.
#
# Key Idea:
#   stack_in: for all pushes
#   stack_out: for all pops/peeks
#   When stack_out is empty, pour all of stack_in into stack_out.
#   This reverses the order → gives FIFO behaviour.

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def _pour(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._pour()
        return self.out_stack.pop()

    def peek(self):
        self._pour()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

q = MyQueue()
q.push(1); q.push(2)
print("\nQ4 peek:", q.peek())   # 1
print("Q4 pop:", q.pop())       # 1
print("Q4 empty:", q.empty())   # False


# ─────────────────────────────────────────────────────────────
# Q5. NEXT GREATER ELEMENT I  (LC #496)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   nums1 is a subset of nums2. For each element in nums1,
#   find the next greater element in nums2 to its right. -1 if none.
#
# Example:
#   nums1=[4,1,2], nums2=[1,3,4,2]  →  [-1,3,-1]
#
# Key Idea (Monotonic Stack + HashMap):
#   Process nums2 with a monotonic stack.
#   Build a map: element → its next greater element in nums2.
#   Then answer for nums1 is just a lookup.

def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    return [next_greater.get(n, -1) for n in nums1]

print("\nQ5:", next_greater_element([4,1,2], [1,3,4,2]))   # [-1,3,-1]
print("Q5:", next_greater_element([2,4], [1,2,3,4]))       # [3,-1]

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 05
# ============================================================
#  Q1  Min Stack                → Time O(1)   Space O(n)
#  Q2  Evaluate RPN             → Time O(n)   Space O(n)
#  Q3  Daily Temperatures       → Time O(n)   Space O(n)
#  Q4  Queue via Stacks         → Time O(1)*  Space O(n)  (*amortized)
#  Q5  Next Greater Element     → Time O(n)   Space O(n)
# ============================================================
