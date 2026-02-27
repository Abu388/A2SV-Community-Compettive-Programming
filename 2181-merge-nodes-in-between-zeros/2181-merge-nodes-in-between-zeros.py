# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head.next
        if not slow:
            return head
        res = 0
        prev = head
        while slow:
            while slow.val != 0:
                res += slow.val
                slow = slow.next
            prev.next = ListNode(res)
            prev = prev.next
            res = 0
            slow = slow.next
        return head.next