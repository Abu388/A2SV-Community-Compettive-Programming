# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

from collections import Counter, defaultdict
from math import ceil
def arr(): return list(map(int, (x for x in input().strip())))
def test(): return int(input())


t=test()
nums=arr()

stk=[]
for i in nums:
 
    if stk and stk[-1]!=i:
        stk.pop()
    else:
        stk.append(i)

print(len(stk))