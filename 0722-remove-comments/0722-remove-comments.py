class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        arr = []
        in_block_comment = False

        for line in source:
            if not in_block_comment:
                res = []  

            i = 0
            while i < len(line):
                if not in_block_comment and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                    
                    break
                elif not in_block_comment and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                    
                    in_block_comment = True
                    i += 1  
                elif in_block_comment and i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                    
                    in_block_comment = False
                    i += 1  
                elif not in_block_comment:
                    
                    res.append(line[i])
                i += 1

            
            if res and not in_block_comment:
                arr.append("".join(res))

        return arr

        
        