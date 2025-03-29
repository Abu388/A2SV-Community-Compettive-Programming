# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix[0])-1   
        t = 0     
        flag = False
        for i in range(len(matrix)):
            if matrix[i][r] == target:
                return True
            elif matrix[i][r] > target:
                l = i
                flag = True
                break
        if not flag:
            return False
        else:
            while t<=r:
                mid = (t+r)//2
                if matrix[l][mid] < target:
                    t += mid + 1
                elif matrix[l][mid] > target:
                    r = mid - 1
                else:
                    return True
        return False

        
        
