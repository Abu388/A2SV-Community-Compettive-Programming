# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gdc(a,b):
            while b != 0:
                a , b = b , a % b
            return abs(a)
        slow = head
        fast = head.next
        if not fast:
            return head
        while fast:
            g = gdc(slow.val, fast.val)
            prev = slow.next
            slow.next = ListNode(g)
            slow = slow.next
            slow.next = prev
            slow = slow.next
            fast = slow.next
        return head
        