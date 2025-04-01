# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

t=test()
for _ in range(t):
    n=test()
    nums=arr()
    ans=[]
    
    
    if nums[0] == 1:
        ans.append(nums[0]+1)
        for i in range(1,len(nums)):
            if ans[i-1]+1 != nums[i] :
                ans.append(ans[i-1]+1)
            else:
                ans.append(ans[i-1]+2)
    else:
        ans.append(1)
        for i in range(1,len(nums)):
            if ans[i-1]+1 != nums[i] :
                ans.append(ans[i-1]+1)
            else:
                ans.append(ans[i-1]+2)

    print(ans[-1])

