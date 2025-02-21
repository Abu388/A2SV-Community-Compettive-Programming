# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy = ListNode() 
        tail = dummy

        greater = ListNode()  
        great_tail = greater

        while head:
            if head.val < x:
                tail.next = head
                tail = tail.next
            else:
                great_tail.next = head
                great_tail = great_tail.next
            head = head.next  
        
        great_tail.next = None
        
        tail.next = greater.next

        return dummy.next
