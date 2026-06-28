# ============================================================
#  DAY 09 — TREES : BFS & DFS  (Asked Almost Everywhere)
#  Pattern : Recursive DFS (preorder/inorder), BFS with queue
# ============================================================

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(arr):
    # Build tree from level-order list (None = missing node)
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


# ─────────────────────────────────────────────────────────────
# Q1. MAXIMUM DEPTH OF BINARY TREE  (LC #104)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return the maximum depth (number of nodes along the longest path).
#
# Example:
#       3
#      / \
#     9  20
#        / \
#       15   7     →  depth = 3
#
# Key Idea (DFS):
#   depth(node) = 1 + max(depth(left), depth(right))
#   Base case: None → 0

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

print("Q1:", max_depth(make_tree([3,9,20,None,None,15,7])))   # 3


# ─────────────────────────────────────────────────────────────
# Q2. INVERT BINARY TREE  (LC #226)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Invert (mirror) a binary tree.
#
# Example:
#     4               4
#    / \     →       / \
#   2   7           7   2
#  / \ / \         / \ / \
# 1  3 6  9       9  6 3  1
#
# Key Idea (DFS):
#   Swap left and right children, then recurse into both subtrees.

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left   # swap
    invert_tree(root.left)
    invert_tree(root.right)
    return root

inverted = invert_tree(make_tree([4,2,7,1,3,6,9]))
print("Q2:", inverted.val, inverted.left.val, inverted.right.val)   # 4, 7, 2


# ─────────────────────────────────────────────────────────────
# Q3. SAME TREE  (LC #100)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given two binary trees, return True if they are identical.
#
# Example:
#   [1,2,3] and [1,2,3]  →  True
#   [1,2]   and [1,None,2]  →  False
#
# Key Idea (DFS):
#   Both None → True
#   One None  → False
#   Values differ → False
#   Else: recurse left and right

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

print("\nQ3:", is_same_tree(make_tree([1,2,3]), make_tree([1,2,3])))       # True
print("Q3:", is_same_tree(make_tree([1,2]), make_tree([1,None,2])))        # False


# ─────────────────────────────────────────────────────────────
# Q4. LEVEL ORDER TRAVERSAL  (LC #102)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return the level-order (BFS) traversal as list of lists.
#
# Example:
#       3
#      / \
#     9  20
#        / \
#       15   7    →   [[3], [9,20], [15,7]]
#
# Key Idea (BFS with Queue):
#   Use a deque. Each iteration processes ALL nodes at the current level.
#   For each node, add its children to the queue for the next level.

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

print("\nQ4:", level_order(make_tree([3,9,20,None,None,15,7])))  # [[3],[9,20],[15,7]]


# ─────────────────────────────────────────────────────────────
# Q5. VALIDATE BINARY SEARCH TREE  (LC #98)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Given a binary tree, return True if it's a valid BST.
#   BST rule: left subtree values < node < right subtree values.
#
# Example:
#     2
#    / \
#   1   3   →  True
#
#     5
#    / \
#   1   4
#      / \
#     3   6  →  False  (3 < 5 violates root constraint in right subtree)
#
# Key Idea:
#   Pass down valid (min, max) range for each node.
#   If node.val not in (min, max) range → invalid.

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (is_valid_bst(root.left,  min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

print("\nQ5:", is_valid_bst(make_tree([2,1,3])))           # True
print("Q5:", is_valid_bst(make_tree([5,1,4,None,None,3,6])))  # False

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 09
# ============================================================
#  Q1  Max Depth            → Time O(n)   Space O(h)  h=tree height
#  Q2  Invert Tree          → Time O(n)   Space O(h)
#  Q3  Same Tree            → Time O(n)   Space O(h)
#  Q4  Level Order (BFS)    → Time O(n)   Space O(n)
#  Q5  Validate BST         → Time O(n)   Space O(h)
# ============================================================
