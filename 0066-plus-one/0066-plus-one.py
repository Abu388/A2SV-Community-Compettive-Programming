class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        y= ''
        for i in digits:
            y+=str(i)
        z=int(y)+1
        z=[int(c) for c in str(z)]
        return z


       
        