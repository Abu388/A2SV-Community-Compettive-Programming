# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        dummy=ListNode()
        dummy.next=head
        first=dummy
        res=dummy
    
        while n>=0 and first:
            first=first.next
            n-=1


        while first and res:
            res=res.next
            first=first.next

        res.next=res.next.next
         
        return dummy.next

       