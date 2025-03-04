# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total=0
        n=maxDoubles 
        if maxDoubles==0:
            return target -1

        while target>0:
            if target % 2==0:
                total+=1
                target=(target//2)
                maxDoubles-=1
            else:
                total+=1
                target-=1
            
            if maxDoubles==0:
                return (total+target-1)
        
        return total-1
