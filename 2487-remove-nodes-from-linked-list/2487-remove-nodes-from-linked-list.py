# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        slow = head
        dummy = ListNode(0)
        prev = dummy
        while slow:
            if not stk:
                stk.append(slow.val)
            else:
                while stk and stk[-1] < slow.val:
                    stk.pop()
                stk.append(slow.val) 
            slow = slow.next
        for v in stk:
            prev.next = ListNode(v)
            prev = prev.next 
        return dummy.next