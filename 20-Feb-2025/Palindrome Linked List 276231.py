# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=slow=head
        helper=head
        prev=None

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if fast==None:
            while slow:
                temp=slow.next
                slow.next=prev
                prev=slow
                slow=temp
            while prev and helper:
                if prev.val != helper.val:
                    return False
                prev,helper=prev.next,helper.next
        elif fast.next==None:
            slow=slow.next
            while slow:
                temp=slow.next
                slow.next=prev
                prev=slow
                slow=temp
            while prev and helper:
                if prev.val != helper.val:
                    return False
                prev,helper=prev.next,helper.next
        return True







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # prev,curr=None,head
        # def deep_copy(node):
        #     if not node:
        #         return None
        #     return ListNode(node.val ,deep_copy(node.next) )
        # deep=deep_copy(head)
        # print(deep.val)
        # while curr:
        #     temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=temp
      
        # while prev:
        #     if prev.val != deep.val:
        #         return False
        #     prev,deep=prev.next,deep.next

        # return True