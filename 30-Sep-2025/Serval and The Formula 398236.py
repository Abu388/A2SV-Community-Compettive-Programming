# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

t= int(input())
for _ in range(t):
    x,y= map(int,input().split())
    if x==y:
        print(-1)
    else:
        if x<y:
            x,y=y,x
        i=1
        while i<x:
            i=i*2
        print(i-x)
