# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))

mp=defaultdict(int)

t= int(input())
for _ in range(t):
    i,j=arr()
    mp[i]+=1
    mp[j]-=1
mp=dict(sorted(mp.items()))
res=0
total=0
for k,v in mp.items():
    total+=v
    res=max(res,total)
    mp[k]=total
for k , v in mp.items():
    if v==res:
        print(k,v)
        break