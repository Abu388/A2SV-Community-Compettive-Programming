# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        ini = -1
        end = len(img)
        arr = [[0] * len(img[0]) for _ in range(len(img))]  # Fixed matrix dimensions
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                res = [img[i][j]]  # Start with the current cell value
                
                # Left and Right
                if j - 1 >= 0:
                    res.append(img[i][j - 1])
                if j + 1 < len(img[0]):
                    res.append(img[i][j + 1])
                
                # Up and Down
                if i - 1 >= 0:
                    res.append(img[i - 1][j])
                if i + 1 < len(img):
                    res.append(img[i + 1][j])
                
                # Diagonal Neighbors
                if i - 1 >= 0 and j - 1 >= 0:
                    res.append(img[i - 1][j - 1])
                if i - 1 >= 0 and j + 1 < len(img[0]):
                    res.append(img[i - 1][j + 1])
                if i + 1 < len(img) and j - 1 >= 0:
                    res.append(img[i + 1][j - 1])
                if i + 1 < len(img) and j + 1 < len(img[0]):
                    res.append(img[i + 1][j + 1])
                
                arr[i][j] = sum(res) // len(res)  # Compute the smoothed value
        
        return arr
