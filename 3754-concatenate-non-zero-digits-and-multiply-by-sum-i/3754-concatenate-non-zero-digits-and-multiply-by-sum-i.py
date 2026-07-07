class Solution:
    def sumAndMultiply(self, n: int) -> int:
        y = ''
        c = 0
        for i in str(n):
            if i != '0':
                y += i
                c += int(i)
        return int(y) * c if y != '' else 0 
        