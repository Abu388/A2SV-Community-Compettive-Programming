class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        val = set()
        t = set()
        res = 0
        word = sorted(word ,reverse = True)
        print(word)
        for s in word:
            if s.islower():
                val.add(s)
            else:
                if s.lower() in val and s not in t:
                    t.add(s.upper())
                    res += 1
        return res
