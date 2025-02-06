# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res=[]
        for i in image:
            
            arr=i[::-1]
            
            for j in range(len(arr)):
                if arr[j]==0:
                    
                    arr[j]=1
                else:
                    arr[j]=0
            res.append(arr)
            
                

        return res
