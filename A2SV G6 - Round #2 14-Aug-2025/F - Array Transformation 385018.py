# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter

def arr(): return list(map(int, input().split()))
def test(): return int(input())

def solve():
    t = test()
    for _ in range(t):
        n = test()
        a = arr()
        
        freq = Counter(a)
        
        freq_counts = Counter(freq.values())
        
        unique_freqs = sorted(freq_counts.keys())
        
        min_removals = float('inf')
        
        for C in unique_freqs:
            total = 0
            for k in unique_freqs:

                if k < C:
                    total += freq_counts[k] * k

                else:
                    total += freq_counts[k] * (k - C)

            if total < min_removals:
                min_removals = total
        
        print(min_removals)

solve()