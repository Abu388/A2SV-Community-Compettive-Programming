# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

from collections import Counter, defaultdict
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))
def test(): return int(input())
n,s=arr()
res=0

while s!=0 :
    if s>=n:
        res+=1
        
        s=s-n
           
    else:
        n-=1
print(res)