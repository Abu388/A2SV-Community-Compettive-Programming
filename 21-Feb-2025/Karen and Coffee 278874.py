# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,r=map(int,input().split())
c=[0]*200004
recipes= [list(map(int,input().split())) for _ in range(n)]
quires = [list(map(int,input().split())) for _ in range(r)]


for start,end in recipes:
    c[start]+=1
    c[end+1]-=1

for i in range(len(c)):
    c[i]+=c[i-1]

for i in range(len(c)):
    if c[i]>=k:
        c[i]=1
    else:
        c[i]=0

for i in range(1,len(c)):
    c[i]+=c[i-1]

for left,right in quires:
    if left==0:
        print(c[right])
    else:
        print(c[right]-c[left-1])






