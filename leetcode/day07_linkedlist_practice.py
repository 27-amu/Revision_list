# ============================================================
#  DAY 07 — LINKED LIST  PRACTICE FILE
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


# Q1. REVERSE LINKED LIST  (LC #206)
# 1→2→3→4→5  →  5→4→3→2→1
# Hint: prev=None, curr=head — save next, flip pointer, advance

def reverse_list(head):
    pass


# Q2. MERGE TWO SORTED LISTS  (LC #21)
# 1→2→4 + 1→3→4  →  1→1→2→3→4→4
# Hint: dummy node, compare l1/l2, attach smaller, advance that pointer

def merge_two_lists(l1, l2):
    pass


# Q3. LINKED LIST CYCLE  (LC #141)
# Return True if cycle exists
# Hint: slow/fast pointers — if they meet, cycle exists

def has_cycle(head):
    pass


# Q4. MIDDLE OF THE LINKED LIST  (LC #876)
# 1→2→3→4→5  →  node with val 3
# Hint: slow moves 1 step, fast moves 2 — when fast ends, slow = middle

def middle_node(head):
    pass


# Q5. REMOVE NTH NODE FROM END  (LC #19)
# 1→2→3→4→5, n=2  →  1→2→3→5
# Hint: dummy node, move fast n+1 ahead, then move both until fast=None

def remove_nth_from_end(head, n):
    pass


# ── TEST YOUR CODE ──────────────────────────────────────────
print_list(reverse_list(make_list([1,2,3,4,5])))                  # [5,4,3,2,1]
print_list(merge_two_lists(make_list([1,2,4]), make_list([1,3,4]))) # [1,1,2,3,4,4]
print(has_cycle(make_list([1, 2])))                               # False
print(middle_node(make_list([1,2,3,4,5])).val)                    # 3
print_list(remove_nth_from_end(make_list([1,2,3,4,5]), 2))        # [1,2,3,5]
