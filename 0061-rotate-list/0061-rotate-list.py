# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Count length
        count = 1
        move = head
        while move.next:
            move = move.next
            count += 1

        # Connect tail to head (make circular)
        move.next = head

        # Reduce k
        k = k % count
        steps = count - k

        # Find new tail
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next
        new_tail.next = None

        return new_head