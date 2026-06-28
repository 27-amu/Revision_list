# ============================================================
#  DAY 09 — TREES  PRACTICE FILE
# ============================================================

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


# Q1. MAXIMUM DEPTH OF BINARY TREE  (LC #104)
# [3,9,20,None,None,15,7]  →  3
# Hint: return 1 + max(depth(left), depth(right)), base case None→0

def max_depth(root):
    pass


# Q2. INVERT BINARY TREE  (LC #226)
# Mirror the tree — swap left/right at every node
# Hint: swap root.left and root.right, then recurse both sides

def invert_tree(root):
    pass


# Q3. SAME TREE  (LC #100)
# [1,2,3] and [1,2,3]  →  True
# Hint: both None=True, one None=False, values differ=False, recurse

def is_same_tree(p, q):
    pass


# Q4. LEVEL ORDER TRAVERSAL  (LC #102)
# [3,9,20,None,None,15,7]  →  [[3],[9,20],[15,7]]
# Hint: BFS with deque, process all nodes at current level together

def level_order(root):
    pass


# Q5. VALIDATE BINARY SEARCH TREE  (LC #98)
# [2,1,3]  →  True  |  [5,1,4,None,None,3,6]  →  False
# Hint: pass (min_val, max_val) range down; node.val must be in range

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print(max_depth(make_tree([3,9,20,None,None,15,7])))          # 3
inverted = invert_tree(make_tree([4,2,7,1,3,6,9]))
print(inverted.left.val, inverted.right.val)                  # 7, 2
print(is_same_tree(make_tree([1,2,3]), make_tree([1,2,3])))   # True
print(level_order(make_tree([3,9,20,None,None,15,7])))        # [[3],[9,20],[15,7]]
print(is_valid_bst(make_tree([2,1,3])))                       # True
