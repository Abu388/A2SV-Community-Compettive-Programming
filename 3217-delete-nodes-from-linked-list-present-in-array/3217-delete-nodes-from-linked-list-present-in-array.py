# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num = set(nums)
        dummy = ListNode()
        prev = dummy
        slow = head
        while slow:
            if slow.val not in num:
                prev.next = ListNode(slow.val)
                prev = prev.next
            slow = slow.next
        return dummy.next
        