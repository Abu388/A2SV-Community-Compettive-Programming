# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))

mp=defaultdict(int)
final=defaultdict(int)
t= int(input())
for _ in range(t):
    i,j=arr()
    mp[i]+=1
    mp[j+1]-=1
mp=dict(sorted(mp.items()))

key=list(mp.keys())
values=list(mp.values())
for i in range(1, len(values)):
    values[i] += values[i - 1]

final = defaultdict(int)
for i in range(len(key) - 1):
    active = values[i]
    length = key[i + 1] - key[i]
    final[active] += length
    
res=[0]*t
for k, v in final.items():
    if 1 <= k <= t:
        res[k - 1] = v

   

print(*res)