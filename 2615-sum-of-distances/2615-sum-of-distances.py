class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(nums)):
            mp[nums[i]].append(i)  
        res = [0] * len(nums)
        
        for val in mp.values():
            n = len(val)

            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + val[i]
            
            for i in range(n):
                left = val[i] * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - val[i] * (n - i - 1)
                res[val[i]] = left + right
        
        return res