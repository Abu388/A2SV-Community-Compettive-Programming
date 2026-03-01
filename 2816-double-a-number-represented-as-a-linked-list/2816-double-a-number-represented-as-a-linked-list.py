# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = str()
        slow = head
        while slow:
            res += str(slow.val)
            slow = slow.next
        res = int(res) * 2
        dummy = ListNode()
        prev = dummy
        for r in str(res):
            prev.next = ListNode(int(r))
            prev = prev.next
        return dummy.next

