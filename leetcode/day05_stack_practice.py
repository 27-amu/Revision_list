# ============================================================
#  DAY 05 — STACK & QUEUE  PRACTICE FILE
# ============================================================


# Q1. MIN STACK  (LC #155)
# push, pop, top, getMin — all O(1)
# Hint: maintain a second stack that always holds the current minimum

class MinStack:
    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def getMin(self):
        pass


# Q2. EVALUATE REVERSE POLISH NOTATION  (LC #150)
# ["2","1","+","3","*"]  →  9
# Hint: push numbers, on operator pop two and push result

def eval_rpn(tokens):
    pass


# Q3. DAILY TEMPERATURES  (LC #739)
# [73,74,75,71,69,72,76,73]  →  [1,1,4,2,1,1,0,0]
# Hint: monotonic stack of indices, pop when current temp is warmer

def daily_temperatures(temps):
    pass


# Q4. IMPLEMENT QUEUE USING STACKS  (LC #232)
# push, pop, peek, empty — FIFO using two LIFO stacks
# Hint: in_stack for push, out_stack for pop/peek; pour when out is empty

class MyQueue:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def empty(self):
        pass


# Q5. NEXT GREATER ELEMENT I  (LC #496)
# nums1=[4,1,2], nums2=[1,3,4,2]  →  [-1,3,-1]
# Hint: build next_greater map from nums2 using monotonic stack

def next_greater_element(nums1, nums2):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
ms = MinStack()
ms.push(-2); ms.push(0); ms.push(-3)
print(ms.getMin())                                          # -3
ms.pop()
print(ms.top(), ms.getMin())                                # 0, -2

print(eval_rpn(["2","1","+","3","*"]))                     # 9
print(daily_temperatures([73,74,75,71,69,72,76,73]))       # [1,1,4,2,1,1,0,0]

q = MyQueue()
q.push(1); q.push(2)
print(q.peek(), q.pop(), q.empty())                        # 1, 1, False

print(next_greater_element([4,1,2], [1,3,4,2]))            # [-1,3,-1]
