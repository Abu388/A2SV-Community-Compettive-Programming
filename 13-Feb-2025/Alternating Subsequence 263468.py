# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t= int(input())
for _ in range(t):
    n =  int(input())
    nums= list(map(int, input().split()))
    l=1
    last=nums[0]
    arr=[]
    
    while l < len(nums):
        if nums[l]*last>0:
            last=max(last,nums[l])
        else:
            arr.append(last)
            last=nums[l]
        l+=1



        
    print(sum(arr[:])+last)
   