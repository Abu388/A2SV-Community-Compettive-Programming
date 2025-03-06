# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        ans=[0]*len(temperatures)
        for l, i in enumerate(temperatures):
            while stk  and stk[-1][0]<i:
                val,ind=stk.pop()
                ans[ind]=l-ind
            stk.append((i,l))
        return ans

            
            

            


