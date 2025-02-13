# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        def Halper(left,right):
            while left<=right:
                if s[left] !=s[right]:
                    return False
                left+=1
                right-=1
            return True


        while l <= r:
            if s[l]!=s[r]:
                return Halper(l+1,r) or Halper(l,r-1)
            l+=1
            r-=1
        return True