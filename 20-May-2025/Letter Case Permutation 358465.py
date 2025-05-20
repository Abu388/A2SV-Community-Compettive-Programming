# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(index: int, path: str):
            if index == len(s):
                res.append(path)
                return

            if s[index].isdigit():
                backtrack(index + 1, path + s[index])
            else:
                backtrack(index + 1, path + s[index].lower())
                backtrack(index + 1, path + s[index].upper())

        backtrack(0, "")
        return res
