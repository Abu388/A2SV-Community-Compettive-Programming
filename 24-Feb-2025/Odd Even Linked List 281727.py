# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd=head
        right=head.next
        change=right
        even=change
        while right and right.next:
            odd.next=right.next
            odd=odd.next
            right.next=odd.next
            right =right.next
        odd.next=even
        return head