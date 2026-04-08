# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy

        current1 = l1
        current2 = l2
        val1 = ''
        val2 = ''

        # build string for list1
        while current1:
            val1 += str(current1.val)
            current1 = current1.next
        
        # build string for list2
        while current2:
            val2 += str(current2.val)
            current2 = current2.next
        
        # reverse both strings to get actual numbers
        total = int(val1[::-1]) + int(val2[::-1])

        # create new linked list from result (in reverse order again)
        for d in str(total)[::-1]:
            pointer.next = ListNode(int(d))
            pointer = pointer.next

        return dummy.next