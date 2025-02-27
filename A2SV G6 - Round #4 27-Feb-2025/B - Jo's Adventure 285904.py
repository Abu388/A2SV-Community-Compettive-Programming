# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))

n,m=arr()
nums=arr()
summation=[0]
suffix=[0]*n
for i in range(n-1):
    if nums[i+1]>=nums[i]:
        summation.append(0)
    else:
        summation.append(nums[i]-nums[i+1])
for i in range(n-1,0,-1):
    if nums[i-1]<nums[i]:
        suffix[i-1]=nums[i]-nums[i-1]

for i in range(1,len(summation)):
    summation[i]+=summation[i-1]
for i in range(n-1,0,-1):
   
    suffix[i-1]+=suffix[i]

for _ in range(m):
    l,r=arr()
    if l<=r:
        print(summation[r-1]-summation[l-1])
    else:
        print(suffix[r-1]-suffix[l-1])

