# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n,m = len(matrix), len(matrix[0])
        arr=[]
        if len(matrix)==1:
            return matrix[0]
        

        if len(matrix[0])<2:
            for t in range(len(matrix)):
                arr.append(matrix[t][0])
            return arr
        vr,vc=0,0
        di=0
        vis = set()
        while di < min((n+1)//2, (m+1)//2):
            for i in range(vc,len(matrix[0])-vc): # right
                if (vr,i) not in vis:
                    arr.append(matrix[vr][i])
                    vis.add((vr,i))
            for j in range(1+vr,len(matrix)-vr): # down
                if (j,m-1-vc) not in vis:
                    arr.append(matrix[j][m-1-vc])
                    vis.add((j,m-1-vc))
            for k in range(len(matrix[0])-2-vc,-1+vc,-1): # left
                if (n-1-vr,k) not in vis:
                    arr.append(matrix[n-1-vr][k])
                    vis.add((n-1-vr,k))

            for u in range(len(matrix)-2-vr,0+vr,-1): # up
                if (u,vc) not in vis:
                    arr.append(matrix[u][vc])
                    vis.add((u,vc))
            vr+=1
            vc+=1
            di+=1
        

        return arr





        # if len(matrix)>2:
        #     for v in range(1,len(matrix[0])-1): # inside
        #         arr.append(matrix[u][v])
        


        # return arr
        






        # for i in range(1,len(matrix[0])):
        #     arr.append(matrix[0][i-1])

        # for j in range(len(matrix)):
        #     arr.append(matrix[j][i])
        # for k in range(len(matrix[0]) - 2, -1, -1): 
        #     arr.append(matrix[j][k])
        # for up in range(len(matrix) - 2, 0 ,-1):
        #     arr.append(matrix[up][k])
        # for left in range(1,len(matrix[0])-1):
        #     arr.append(matrix[up][left])
        # return arr
        
        
        
            

        

            
        
        