# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        
        def valid(part):
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) < 256

        def bkt(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return

            for l in range(1, 4):
                if start + l > len(s):
                    break
                part = s[start:start+l]
                if valid(part):
                    bkt(start+l, path + [part])
        
        bkt(0, [])
        return res
