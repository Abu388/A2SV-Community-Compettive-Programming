class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd = defaultdict(int)
        eve = defaultdict(int)
        odd2 = defaultdict(int)
        eve2 = defaultdict(int)
        for i in range(len(s1)):
            if i % 2:
                odd[s1[i]] += 1
            else:
                eve[s1[i]] += 1
        for i in range(len(s2)):
            if i % 2:
                odd2[s2[i]] += 1
            else:
                eve2[s2[i]] += 1
        
        return odd == odd2 and eve == eve2

