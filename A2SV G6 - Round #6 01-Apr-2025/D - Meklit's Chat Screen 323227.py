# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))
def test(): return int(input())


stk=deque()
n,k=arr()
nums=arr()
helper=set()

for i in nums:
    
    if i not in helper and len(stk) < k:#o(n^2) chaking so what shall i do?:
        stk.appendleft(i)
        helper.add(i)
    elif i not in helper:
        stk.appendleft(i)   
        helper.add(i)
        temp  = stk.pop()
        helper.remove(temp)
        
print(len(stk))
print(*stk)