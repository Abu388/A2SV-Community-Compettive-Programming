class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        arr = []
        in_block_comment = False

        for line in source:
            if not in_block_comment:
                res = []  # Start a new line if not inside a block comment

            i = 0
            while i < len(line):
                if not in_block_comment and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                    
                    break
                elif not in_block_comment and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                    # Start of a block comment
                    in_block_comment = True
                    i += 1  # Skip next character ('*')
                elif in_block_comment and i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                    # End of a block comment
                    in_block_comment = False
                    i += 1  # Skip next character ('/')
                elif not in_block_comment:
                    # Normal character outside of any comment
                    res.append(line[i])
                i += 1

            # If not in a block comment and line has content, add to result
            if res and not in_block_comment:
                arr.append("".join(res))

        return arr

        
        