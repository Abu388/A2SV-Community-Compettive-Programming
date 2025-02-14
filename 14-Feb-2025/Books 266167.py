# Problem: Books - https://codeforces.com/contest/279/problem/B

n,target= map(int,input().split())
nums=list(map(int,input().split()))
r=0
l=0
count=0
total_book=float('-inf')
for r in range(len(nums)):
    count+=nums[r]
    
    while count>target:
        count-= nums[l]
        l+=1
    total_book=max(total_book,r-l+1)
print(total_book)

