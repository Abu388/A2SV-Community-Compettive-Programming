# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l,r=0,len(people)-1
        while r>=l:
            remainder = limit - people[r]
            res+=1
            r-=1
            if r>=l and remainder >=people[l]:
                l+=1
        return res
        