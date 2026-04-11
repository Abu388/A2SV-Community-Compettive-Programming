class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        res = float('inf')
        mp = defaultdict(list)
        for i in range(len(nums)):
            mp[nums[i]].append(i)
        for ke in mp.keys():
            if len(mp[ke]) >= 3:
                val = mp[ke]
                l = 0
                while l <= len(val) - 3:
                    i , j , k = val[0 + l], val[1 + l], val[2 + l]
                    res = min(2 * (max(i, j, k) - min(i, j, k)), res )
                    l += 1
                
        return res if res < float('inf') else - 1