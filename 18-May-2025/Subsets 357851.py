# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
    
        def solu(ind,temp):
            if ind >= n:
                ans.append(temp.copy())
                return 
            # leave it 
            solu(ind+1, temp)
            # take it
            temp.append(nums[ind])
         
            solu(ind + 1, temp)
          
            temp.pop()



        solu(0,[])
        return ans
