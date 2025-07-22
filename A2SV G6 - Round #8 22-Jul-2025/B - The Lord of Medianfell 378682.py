# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B


def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())
t = test()
for _ in range(t):
    n, s = arr()
    k = (n// 2) + 1
    print((s // k))


