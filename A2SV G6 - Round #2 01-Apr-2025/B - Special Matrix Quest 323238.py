# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
res=0
for row in range(n):
    res+=arr[row][row]
    res+=arr[row][n//2]
    res+=arr[n//2][row]
    res+=arr[row][n-1-row]
res-=arr[n//2][n//2]*3
print(res)
