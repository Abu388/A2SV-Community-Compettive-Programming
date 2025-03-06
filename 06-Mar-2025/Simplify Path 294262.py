# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        subdomains = path.split('/')

        resolved_path = []
        for part in subdomains:
            if part == "..":
                if resolved_path:
                    resolved_path.pop()  # Go back one directory
            elif part and part != ".":  # Ignore empty parts and current directory symbol
                resolved_path.append(part)
        if not resolved_path:
            resolved_path.append("/")
            res = "/".join(resolved_path)
            return res
        

        res = "/"+"/".join(resolved_path)
        
        return res