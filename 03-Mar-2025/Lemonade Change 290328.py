# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        has={5:0,10:0,20:0}
  
        for i in bills:
            if i==5:
                has[i]+=1
            elif i==10:
                has[5]-=1
                if has[5]<0:
                    return False
                has[i]+=1
            else:
                has[10]-=1
                if has[10]<0:
                    has[5]-=3
                    if has[5]<0:
                        return False
                    has[10]+=1
                else:
                    has[5]-=1
                    if has[5]<0:
                        return False



            
        return True