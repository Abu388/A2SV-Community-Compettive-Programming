# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

import bisect #arr = [1, 2, 4, 4, 5] , index = bisect.bisect_right(arr, 4)
import sys
from fractions import Fraction # to use fraction
import sys, threading

input = sys.stdin.readline
from heapq import *
from itertools import accumulate # to work on prefix
from collections import Counter, defaultdict,deque
from math import ceil,floor
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())




n , m = list(map(int,input().split()))

parent =[0] + [i for i in range(1,n+2)]
size = [1] * (n + 1)
rank = [0] * (n + 1)

def addition(x):
    val = 0
    val += rank[x] 
    while x != parent[x]:
        x = parent[x]
        val += rank[x]
    # if parent[x] != x:
    #     parent[x] = addition(parent[x]) 
    return val

def find(x):
    if parent[x] != x:
        return find(parent[x]) 
    return parent[x]
def union(x,y):
    xu = find(x)
    yu = find(y)
    if xu != yu:     
        if size[xu] > size[yu]:
            size[xu] += size[yu]
            rank[yu] -= rank[xu]
            parent[yu] = xu
        else:        
            size[yu] += size[xu]
            rank[xu] -= rank[yu]
            parent[xu] = yu
for _ in range(m):
    q = input().split()
    if q[0] == 'get':
        
        print(addition(int(q[1])))
       
    elif q[0] == 'join':
        union(int(q[1]),int(q[2]))
    else:
        
        v = find(int(q[1]))
        rank[v] += int(q[2])
        
        

    










    