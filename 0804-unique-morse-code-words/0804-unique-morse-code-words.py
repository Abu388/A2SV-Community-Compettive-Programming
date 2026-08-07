class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        for i in words:
            y = ''
            for w in i:
                y += tab[ord(w) - 97]
            res.add(y)
        return len(res)
                



