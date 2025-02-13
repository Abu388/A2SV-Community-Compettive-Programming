# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        r=0
        arr=[]
        l=len(skill)-1
        while r<l:
            if skill[l]+skill[r]==skill[l-1]+skill[r+1]:
                arr.append(skill[l]*skill[r])
            else:
                return -1
            r+=1
            l-=1
        
        return sum(arr)