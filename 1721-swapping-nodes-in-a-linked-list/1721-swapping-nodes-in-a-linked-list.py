# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        slow = head
        count = 1
        first = None
        
        while slow:
            if count == k:
                first = slow
            count += 1
            slow = slow.next
        
        second = None
        b = count - k 
        
        c = 1
        last = head
        while last:
            if c == b:
                second = last
            c += 1
            last = last.next
        
        second.val , first.val =  first.val, second.val 
        return head
        
