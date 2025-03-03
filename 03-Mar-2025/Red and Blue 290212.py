# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))
t=int(input())
for _ in range(t):
    n=int(input())
    nums=arr()
    m=int(input())
    nums2=arr()
    pre=[]
    prefix=[]
    total=0
    for i in nums:
        total+=i
        pre.append(total)
    total=0
    for i in nums2:
        total+=i
        prefix.append(total)

    result=max(0,max(pre),max(prefix),max(prefix)+max(pre))
    print(result)