# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A


from math import ceil,floor
def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())

t = test()
for _ in range(t):
    x = test()
    c = 1
    for j in range(32):
        if x & c << j :
            c = c <<j
            break     
    if c ^ x > 0 and c & x > 0:
        print(c)  
    else:
        zero = 1
        for j in range(32):
            if not (x & zero << j):
                zero = zero << j
                break
        print(c+zero)
