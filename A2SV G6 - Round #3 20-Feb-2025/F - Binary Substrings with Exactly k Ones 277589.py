# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k=int(input())
nums=list(map(int,input().strip()))
 
mp = {0:1}
ans = 0
rsum = 0
for i in range(len(nums)):
    rsum+=nums[i]
 
    if rsum-k in mp:
        ans+=mp[rsum-k]
 
    mp[rsum]=mp.get(rsum,0)+1
print(ans)