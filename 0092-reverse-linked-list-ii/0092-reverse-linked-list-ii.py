# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        final = dummy
        start = end = head
        count = 1
        count2 = 1
        while count != left:
            final.next = start
            final = final.next
            start = start.next
            count += 1

        while count2 != right:
            end = end.next
            count2 += 1
        prev = None
        stop = end.next
        while start != stop:
            nxt = start.next 
            start.next = prev
            prev = start
            start = nxt
        

        final.next = prev
        while prev:
            final = final.next
            prev = prev.next
        final.next = stop
        
        return dummy.next

        
        
