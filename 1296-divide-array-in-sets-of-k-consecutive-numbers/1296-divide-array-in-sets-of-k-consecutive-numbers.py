import collections
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        counts = collections.Counter(nums)
        for n in sorted(counts):
            if not counts[n]:
                continue
            temp = counts[n]
            for i in range(n,n+k):
                if counts[i]<1:
                    return False 
                counts[i]-=temp
        return True 
                    
        