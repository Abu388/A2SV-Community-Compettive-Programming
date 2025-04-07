# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def split_number_ways(num):
            number_str = str(num*num)
            n = len(number_str)
            result = []
       

            def backtrack(start, path):
                if start == n:
    
                    
                    if sum(path) == num:
                        y = ""
                        for i in path:
                            y += str(i)
                        
            
                        result.append(y)
                    return
                for end in range(start + 1, n + 1):
                    part = number_str[start:end]
                    path.append(int(part))
                    backtrack(end, path)
                    path.pop()

            backtrack(0, [])
            return result
        total = 0  
        for i in range(1,n+1):
            val = split_number_ways(i)
            
            if val != []:
                total += int(val[0])
        return total
