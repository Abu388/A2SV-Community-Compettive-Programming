# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [chr(97+i) for i in range(26)]

        size = [1] * 26
        def find(x):
            if parent[ord(x)-97] != x:
                parent[ord(x)-97] = find(parent[ord(x)-97])
            return parent[ord(x)-97]
        def union(x,y):
            xu = find(x)
            yu = find(y)
            if ord(xu) == ord(yu):    
                return 
            if ord(xu) < ord(yu):
                parent[ord(yu)-97] = xu
            else:
                parent[ord(xu)-97]= yu
           
                
                
        for i , z in zip(s1,s2):
            union(i,z)
        res = ''
        for i in baseStr:
            res += find(i)
        return res
        
