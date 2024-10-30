class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        l=0
        count=0
        res=0
        while l<len(arr1):
            for i in range(len(arr2)):
                if abs(arr1[l] - arr2[i])>d:
                    count+=1
                else:
                    continue

            if count ==len(arr2):
                res+=1
            l+=1
            count=0
        
        return res 