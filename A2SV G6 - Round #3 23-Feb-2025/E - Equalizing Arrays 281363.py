# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

from collections import Counter, defaultdict
def arr(): return list(map(int, (x for x in input().split())))

def solution(nums1,nums2,one,two):
    if sum(nums1) != sum(nums2):
        return -1
    l,r=0,0
    count=0
    prefix1=[0]*(one)
    prefix2=[0]*(two)
    total=0
    for i in range(one):
        total+=nums1[i]
        prefix1[i]=total
    total=0   
    for i in range(two):
        total+=nums2[i]
        prefix2[i]=total
    

        
    while l<one and r<two:  
        if prefix1[l]==prefix2[r]:
            count+=1
            l+=1
            r+=1
        elif prefix1[l]<prefix2[r]:
            l+=1
        else:
            r+=1
    return count

    
    



one= int(input())
nums1=arr()
two=int(input())
nums2=arr()
print(solution(nums1,nums2,one,two))
