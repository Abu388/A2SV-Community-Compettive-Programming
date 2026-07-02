class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0

        for i in range(len(nums)):
            
            curr = i
            count = 0

            while curr not in visited:
                visited.add(curr)
                curr = nums[curr]
                count += 1

            ans = max(ans, count)

        return ans



        
