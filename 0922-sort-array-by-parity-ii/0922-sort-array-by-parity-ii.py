class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd , eve = [] , []
        for i in nums:
            if i % 2 == 0:
                eve.append(i)
            else:
                odd.append(i)
        res = []
        for i in range(len(odd)):
            res.append(eve[i])
            res.append(odd[i])  
        return res



        