# Problem: Presents - https://codeforces.com/problemset/problem/136/A

def solution(n,arr):
    has={}
    res=[]
    ind=1
    for i in arr:
        has[i]=ind
        ind+=1
    arr.sort()
    
    for j in arr:
        res.append(has[j])

    return res


n= int(input())
arr=list(map(int,input().split()))
print(*solution(n,arr))
