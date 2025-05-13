# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import bisect #arr = [1, 2, 4, 4, 5] , index = bisect.bisect_right(arr, 4)
import sys
from fractions import Fraction # to use fraction
import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
input = sys.stdin.readline
from heapq import *
from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil,floor
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())






n , m = list(map(int,input().split()))

parent =[0] + [i for i in range(1,n+2)]

def find(x):
    if x > n :
        return -1
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]

def union(u, v):


    xu = find(u)
    yu = find(v)
    parent[xu] = parent[yu]

    
    






for _ in range(m):
    val , num = input().split()
    if val == '?':
        print(str(find(int(num))))
    else:
        union(int(num), int(num)+1)


