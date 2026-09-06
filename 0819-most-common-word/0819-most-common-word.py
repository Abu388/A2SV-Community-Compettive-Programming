import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        c = defaultdict(int)

        banned = set(word.lower() for word in banned)

        words = re.findall(r"[a-zA-Z]+", paragraph.lower())

        for word in words:
            c[word] += 1

        for word, count in sorted(c.items(), key=lambda x: x[1], reverse=True):
            if word not in banned:
                return word