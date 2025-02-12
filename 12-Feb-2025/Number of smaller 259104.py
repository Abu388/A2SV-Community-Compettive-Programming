# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m=map(int,input().split())
arr=list(map(int,input().split()))
comp=list(map(int,input().split()))
ind=0
res=[]
for i in comp:
    
    while ind <len(arr) and i>arr[ind] :
        ind+=1
    res.append(ind)
print(*res)