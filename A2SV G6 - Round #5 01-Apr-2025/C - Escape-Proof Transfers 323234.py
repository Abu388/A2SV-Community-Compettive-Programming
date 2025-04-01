# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))

n,t,c=arr()
nums=arr()
count=0
res=0
for i in nums:
    if i<=t:
        count+=1
    else:
        count=0
    if count>=c:
        res+=1
print(res)


