# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n=int(input())
arr=list(map(int,input().split()))
res=float('inf')
for i in arr:
    res=min(abs(i),res)
print(res)