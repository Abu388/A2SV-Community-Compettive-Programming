# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev,curr=None,head
        def deep_copy(node):
            if not node:
                return None
            return ListNode(node.val ,deep_copy(node.next) )
        deep=deep_copy(head)
        print(deep.val)
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
      
        while prev:
            if prev.val != deep.val:
                return False
            prev,deep=prev.next,deep.next

        return True