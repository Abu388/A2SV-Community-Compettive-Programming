# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))
n=int(input())
nums=arr()
nums.sort()
if n %2 !=0:
    print(nums[n//2])
else:
    print(nums[(n//2)-1])