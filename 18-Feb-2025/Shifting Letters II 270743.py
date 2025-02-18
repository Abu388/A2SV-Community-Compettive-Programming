# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre=[0]*(len(s)+1)
        s=list(s)
        for i,e,f in shifts:
            if f==0:
                pre[i]-=1
                pre[e+1]+=1
            else:
                pre[i]+=1
                pre[e+1]-=1
        total=0
     
        for j in range(len(s)):
            total += pre[j]
            new_char = chr((ord(s[j]) - ord('a') + total) % 26 + ord('a'))
            s[j] = new_char
        return ''.join(s)