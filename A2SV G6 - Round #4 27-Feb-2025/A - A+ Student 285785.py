# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))

def findA(a,b,c):
    m=max(0,max(b,c)-a+1)
    return m 
def findB(a,b,c):
    m=max(0,max(a,c)-b+1)
    return m
def findC(a,b,c):
    m=max(0,max(a,b)-c+1)
    return m

t=int(input())
for _ in range(t):
    a,b,c=arr()
    print(findA(a,b,c),findB(a,b,c),findC(a,b,c))
