# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     
        has = {}
        res=[]
        for i in nums:#o(n)
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1
        arr=sorted(has.items() , key=lambda x: x[1])#nlog(n)
        
        a = [key for key, value in arr]
        
        l=len(a)-1
        for i in range(k):
            res.append(a[l])
            l-=1
        return res


        
        



        

        