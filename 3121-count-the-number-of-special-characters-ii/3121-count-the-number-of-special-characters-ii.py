class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low = [-1] * 26
        up = [-1] * 26
        count = 0
        for w in range(len(word)):
            if word[w].islower():
                low[ord(word[w])- 97] = w
            else:
                if up[ord(word[w])- 65 ] == -1:
                    up[ord(word[w]) - 65 ] = w
        for i in range(len(low)):
            if low[i] < up[i] :
                if low[i] != -1 and up[i] != -1:
                    count += 1
        print(low)
        print(up)
        return count


              