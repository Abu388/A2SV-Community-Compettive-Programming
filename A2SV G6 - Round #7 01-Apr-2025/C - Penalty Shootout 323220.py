# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

from collections import Counter, defaultdict,deque
from math import ceil
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

t = test()
for _ in range(t):
    s = input()
    first = []
    second = []
    for i in range(10):
        if i % 2 == 0:
            first.append(s[i])
        else:
            second.append(s[i])
    
    fav1 = 0
    score1 = 0
    score2 = 0
    for i in range(5):
        if first[i] == '1' or first[i] == '?':
            score1+=1
        fav1 += 1
        if score1 > (score2 + 5 - i):
            break
        if second[i] == '1':
            score2+=1
        fav1 += 1
        if score1 > (score2 + 5 - i - 1):
            break
    
    fav2 = 0
    score1 = 0
    score2 = 0
    for i in range(5):
        if first[i] == '1':
            score1 += 1
        fav2 += 1
        if score2 > (score1 + 5 - i - 1):
            break
        if second[i] == '1' or second[i] == '?':
            score2 += 1
        fav2 += 1
        if score2 > (score1 + 5 - i - 1):
            break
    print(min(fav1, fav2))