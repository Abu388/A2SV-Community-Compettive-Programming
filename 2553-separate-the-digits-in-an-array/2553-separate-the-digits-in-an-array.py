class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num=list(map(str,nums))
        
        
        return list(map(int,''.join(num)))
        