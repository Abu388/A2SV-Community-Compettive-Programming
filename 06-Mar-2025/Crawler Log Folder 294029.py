# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in range(len(logs)):
            if logs[i]=="../":
                if count>0:
                    count-=1
                
            elif logs[i] == './':
                count=count
            else:
                count+=1
        return count
            
       
       