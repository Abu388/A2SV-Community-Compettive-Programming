# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        while cur:
            while cur.next and cur.next.val== cur.val:
                cur.next=cur.next.next
            cur=cur.next
        return head


        