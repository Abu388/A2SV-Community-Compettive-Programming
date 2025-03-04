# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total=0
        mp=defaultdict(int)
        for i in answers:
            mp[i]+=1
        for k,v in mp.items():
            value=v%(k+1)
            if value ==0:
                total+=v
            else:
                total+=ceil(v/(k+1))*(k+1)
                

            


        return total



        
