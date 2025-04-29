# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for i , node in enumerate(lists):
            if node:
                heapq.heappush(ans,(node.val ,i, node))
                
        dummy = ListNode(0)
        cur = dummy
        while ans:
            val , i , node = heapq.heappop(ans)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(ans,(node.next.val ,i, node.next))
        return dummy.next


        