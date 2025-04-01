# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

def helper(val):
    if val != 'z':
        return chr(ord(val)+1)
    else:
        return 'a'

t = test()
def good(s,c,l,r):
    if r==l:
        return 1 if s[r]!=c else 0
    mid = (r+l+1) // 2
    length = r-l+1
    m1 = ((length//2) - s[l:mid].count(c)) + good(s,helper(c),mid,r)
    m2 = (length//2) - s[mid:r+1].count(c) + good(s,helper(c),l,mid-1)
    return min(m1,m2)
for _ in range(t):
    n = test()
    s = input()
    c ,l , r= 'a' , 0, len(s)-1
    print(good(s,c,l,r))