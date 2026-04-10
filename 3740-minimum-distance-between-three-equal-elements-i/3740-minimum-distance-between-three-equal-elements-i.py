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
                for i in range(len(val) - 2):
                    for j in range(i + 1, len(val) - 1):
                        for k in range(j + 1 ,len(val)):                
                            res = min(abs(val[i] - val[j]) + abs(val[j] - val[k]) + abs(val[k] - val[i]), res )
            
        return res if res < float('inf') else - 1