# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n= list(map(int,input().split()))
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))

def solu(arr,arr2):
    res=[]
    l=0
    r=0
    while r<len(arr2) and l<len(arr):
        if arr[l]>arr2[r]:
            res.append(arr2[r])
            r+=1
        elif arr[l]<arr2[r]:
            res.append(arr[l])
            l+=1
        else:
            res.append(arr2[r])
            res.append(arr[l])
            r+=1
            l+=1
    res.extend(arr2[r::])
    res.extend(arr[l::])
    return ' '.join(map(str, res))


print(solu(arr,arr2))