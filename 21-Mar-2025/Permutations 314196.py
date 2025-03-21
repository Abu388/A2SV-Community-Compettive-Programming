# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def solu(i,arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return            
            
            for j in range(0,len(nums)):
                if nums[j] in arr:
                    continue
                else:
                    arr.append(nums[j])              
                    solu(i+1 , arr)
                    arr.pop()
                
               


        solu(1,[])
        return res
    














        # arr = [nums[0]]
        # ini = 0
        # if not nums:
        #     return res
        
        # def solu(i, arr):
        #     if len(arr) == n:
        #         res.append(arr.copy())
        #         return
        #     while ini < n:
        #         for j in range(i,n):
        #             arr.append(nums[ind+j])
        #             solu(ind+j,arr)
        #         ind += 1

        # solu(0, [])
        # print(arr)

        