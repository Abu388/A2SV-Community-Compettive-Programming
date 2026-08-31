# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l = ListNode(0)
        l.next = head
        res = []
        c = 1
        h = head
        while h.next:
            if l.val == 0:
                h = h.next
                l = l.next
                c += 1
                continue
            r = h.next
            if l.val < h.val > r.val:
                res.append(c)
            elif l.val > h.val < r.val:
                res.append(c)
            c += 1
            h = h.next
            l = l.next
        if len(res) < 2:
            return [-1,-1]
        elif len(res) == 2:
            return [res[1] - res[0],res[1] - res[0]]
        else:
            mi,ma = float('inf'), 0
            for i in range(1,len(res)):
                mi = min(res[i] - res[i - 1], mi)
               
            return [mi, res[len(res) - 1] - res[0]]
            


        