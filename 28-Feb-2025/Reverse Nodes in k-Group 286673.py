# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        res=dummy
        first=head
        second=head
        while first:

            prev=None
            i=k

            while first and  i>0:
                first=first.next
                i-=1

            if i>0:
                break

            t=k
            while second and t>0 :
                temp=second.next
                second.next=prev
                prev=second
                second=temp
                t-=1
           

            while prev:
                res.next=prev
                prev=prev.next
                res=res.next
        res.next=second
        


        return dummy.next