# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from collections import deque

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    min_deque = deque()
    max_deque = deque()
    res = 0
    l = 0
    
    for r in range(n):
  
        while min_deque and a[r] < a[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(r)
        
        while max_deque and a[r] > a[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(r)
        
        while l <= r and a[max_deque[0]] - a[min_deque[0]] > k:
            l += 1
            
            while min_deque and min_deque[0] < l:
                min_deque.popleft()
            while max_deque and max_deque[0] < l:
                max_deque.popleft()
        
        res += r - l + 1
    
    print(res)

solve()