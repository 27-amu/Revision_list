# ============================================================
#  DAY 07 — LINKED LIST  (Asked Almost Everywhere)
#  Pattern : Fast/Slow pointers, reversal, dummy node
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


# ─────────────────────────────────────────────────────────────
# Q1. REVERSE LINKED LIST  (LC #206)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Reverse a singly linked list. Return the new head.
#
# Example:
#   1→2→3→4→5  →  5→4→3→2→1
#
# Key Idea:
#   Keep three pointers: prev=None, curr=head, next_node.
#   At each step: save next, point curr.next to prev, advance both.

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next    # save next
        curr.next = prev         # reverse pointer
        prev = curr              # advance prev
        curr = next_node         # advance curr
    return prev                  # prev is new head

print_list(reverse_list(make_list([1,2,3,4,5])))   # [5,4,3,2,1]


# ─────────────────────────────────────────────────────────────
# Q2. MERGE TWO SORTED LISTS  (LC #21)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Merge two sorted linked lists into one sorted list.
#
# Example:
#   1→2→4  and  1→3→4  →  1→1→2→3→4→4
#
# Key Idea (Dummy Node):
#   Use a dummy head node to avoid edge cases.
#   Compare l1 and l2 values, attach the smaller one, advance that pointer.

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2         # attach the remaining list
    return dummy.next

print_list(merge_two_lists(make_list([1,2,4]), make_list([1,3,4])))  # [1,1,2,3,4,4]


# ─────────────────────────────────────────────────────────────
# Q3. LINKED LIST CYCLE  (LC #141)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return True if the linked list has a cycle.
#
# Key Idea (Floyd's Cycle Detection — Fast/Slow Pointers):
#   slow moves 1 step, fast moves 2 steps.
#   If there is a cycle, fast will eventually lap slow and they'll meet.
#   If fast reaches None → no cycle.

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Build a cycle manually for testing
cycle_head = make_list([3, 2, 0, -4])
cycle_head.next.next.next.next = cycle_head.next   # -4 → 2 (cycle)
print("\nQ3 (cycle):", has_cycle(cycle_head))           # True
print("Q3 (no cycle):", has_cycle(make_list([1, 2])))  # False


# ─────────────────────────────────────────────────────────────
# Q4. MIDDLE OF THE LINKED LIST  (LC #876)  —  Easy
# ─────────────────────────────────────────────────────────────
# Problem:
#   Return the middle node of the linked list.
#   If two middles exist, return the second one.
#
# Example:
#   1→2→3→4→5  →  node 3
#   1→2→3→4    →  node 3
#
# Key Idea (Fast/Slow Pointers):
#   When fast reaches the end, slow is at the middle.
#   fast moves 2x the speed of slow.

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

mid = middle_node(make_list([1,2,3,4,5]))
print("\nQ4:", mid.val)   # 3

mid = middle_node(make_list([1,2,3,4]))
print("Q4:", mid.val)     # 3


# ─────────────────────────────────────────────────────────────
# Q5. REMOVE NTH NODE FROM END  (LC #19)  —  Medium
# ─────────────────────────────────────────────────────────────
# Problem:
#   Remove the nth node from the end of the list. Return head.
#
# Example:
#   1→2→3→4→5, n=2  →  1→2→3→5
#
# Key Idea (Two Pointers with gap of n):
#   Use dummy node. Advance fast n+1 steps ahead.
#   Move both slow and fast together until fast is None.
#   Now slow.next is the node to remove → slow.next = slow.next.next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    for _ in range(n + 1):         # move fast n+1 ahead
        fast = fast.next
    while fast:                    # move both until fast is None
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next     # skip the target node
    return dummy.next

print_list(remove_nth_from_end(make_list([1,2,3,4,5]), 2))  # [1,2,3,5]

# ============================================================
#  COMPLEXITY CHEAT SHEET — DAY 07
# ============================================================
#  Q1  Reverse Linked List      → Time O(n)   Space O(1)
#  Q2  Merge Two Sorted Lists   → Time O(n)   Space O(1)
#  Q3  Linked List Cycle        → Time O(n)   Space O(1)
#  Q4  Middle of Linked List    → Time O(n)   Space O(1)
#  Q5  Remove Nth From End      → Time O(n)   Space O(1)
# ============================================================
