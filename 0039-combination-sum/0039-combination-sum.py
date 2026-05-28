class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        nums=candidates
        n=len(nums)

        def backtrack(i,cur):
            if cur == target:
                res.append(sol[:])
                return 
            if cur > target or i ==n:
                return
            
            backtrack(i+1,cur)

            sol.append(nums[i])
            backtrack(i,cur+nums[i])
            sol.pop()
        backtrack(0,0)
        return res



        
        