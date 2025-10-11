# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for i in s:
            if not stk:
                stk.append([i,1])
            else:
                if stk[-1][0] == i:
                    if stk[-1][1] == k - 1:
                        for _ in range(k - 1):
                            stk.pop()
                    else:
                        stk.append([i,stk[-1][1] + 1])

                else:
                    stk.append([i,1])
            

                
        
        return ''.join(k  for k , v in stk )
