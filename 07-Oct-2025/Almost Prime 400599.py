# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())




def trial_division_simple(n) :
    factorization = set()
    d = 2
    while d * d <= n:

        while n % d == 0:
            
            factorization.add(d)
            
            n //= d

        d += 1
    if n > 1:
        factorization.add(n)
        
    
    return factorization



t = test()
c = 0
for i in range(4, t + 1):
    res = trial_division_simple(i)
    if len(res) == 2:
        c += 1
print(c)
