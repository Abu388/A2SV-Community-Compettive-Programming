# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        while cur:

            if cur.child:
                next_node = cur.next

                child_tail = cur.child
                while child_tail.next:
                    child_tail = child_tail.next

                # Connect tail to next node
                child_tail.next = next_node
                if next_node:
                    next_node.prev = child_tail

               

                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None

            cur = cur.next
        return head