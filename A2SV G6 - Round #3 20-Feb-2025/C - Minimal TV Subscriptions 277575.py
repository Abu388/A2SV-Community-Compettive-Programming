# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
def solution(nums,n,d):
    
    res=float('inf')
 
    count=Counter(nums[:d-1])
   
    res=float('inf')
    ind=0
    for r in range(d-1,n):  
        count[nums[r]]+=1
        
        res=min(len(count.values()),res)
        count[nums[ind]]-=1
        if count[nums[ind]]==0:
            del count[nums[ind]]
      
        ind+=1
 
    return res
 
t = int(input())
for _ in range(t):
    n,k,d=map(int,input().split())
    nums=list(map(int,input().split()))
    print(solution(nums,n,d))