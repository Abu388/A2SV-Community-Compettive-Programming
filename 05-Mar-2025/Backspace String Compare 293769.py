# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr=[]
        nums=[]
        for i in s:
            if i =='#':
                if len(arr)>0:
                    arr.pop()
            else:
                arr.append(i)
        for i in t:
            if i =='#':
                if len(nums)>0:
                    nums.pop()
            else:
                nums.append(i)
        if nums==arr:
            return True
        return False
        