# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))
def solution(n,k,arr):
    freq = defaultdict(int)
    left = 0
    max_len = 0
    result_l, result_r = 0, 0
 
    for right in range(n):
        freq[a[right]] += 1
 
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
 
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            result_l, result_r = left + 1, right + 1  # +1 because the problem uses 1-based indexing
 
    return result_l, result_r
n,k=arr()
a=arr()
print(*solution(n,k,arr))