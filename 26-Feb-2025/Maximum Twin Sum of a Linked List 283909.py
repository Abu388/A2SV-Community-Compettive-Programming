# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev=None
        total=0
        first=head 
        second=head
        start=head
        while first and first.next:
            second=second.next
            first=first.next.next
        
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        while prev:
            val=prev.val+start.val
            total=max(total,val)
            prev=prev.next
            start=start.next
        return total

    
        