# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        val = {}
        visited = set()
        for i in range(len(t)):
            if s[i] not in val:
                if t[i] not in visited:
                    val[s[i]] = t[i]
                    visited.add(t[i])
                else:
                    return False
            else:            
                if val[s[i]] != t[i]:
                    return False

        return True
