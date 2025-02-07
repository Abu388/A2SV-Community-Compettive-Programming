# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/


class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat == target:
            return True
        
        for _ in range(4):     
            arr=[[0]*len(mat[0]) for _ in range(len(mat))]   
            for j in range(len(mat)):
                col=0
                for i in range(len(mat)-1,-1,-1):
                    arr[j][col]=mat[i][j]
                    
                    col+=1
            mat=arr
            
            if mat== target:
                return True
        return False
  

            
    

                

                
