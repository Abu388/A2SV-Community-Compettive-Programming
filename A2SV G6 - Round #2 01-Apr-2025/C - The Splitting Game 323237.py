# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    left_set = Counter()
    right_count = Counter(s)
    max_sum = 0
    
  
    for i in range(n - 1):
        left_set[s[i]]+=1      
        right_count[s[i]] -= 1  
        
        if right_count[s[i]] == 0:
            del right_count[s[i]]  
        
       
        current_sum = len(left_set) + len(right_count)
        max_sum = max(max_sum, current_sum)
    
    print(max_sum)