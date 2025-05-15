# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]: 
        
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        
        res = []
        for i , j in queries:
            l = 0 if i == 0 else arr[i-1]
            res.append(l ^ arr[j])
        return res
        