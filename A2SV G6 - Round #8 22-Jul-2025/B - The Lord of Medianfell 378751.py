# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

from math import floor

def arr(): 
    return list(map(int, input().split()))

def test(): 
    return int(input())

t = test()
for _ in range(t):
    n, s = arr()
    m = (n // 2) + 1  
    max_median = s // m
    print(max_median)






