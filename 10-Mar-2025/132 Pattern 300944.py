# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk=[]
        minimum=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]<minimum[-1]:
                minimum.append(nums[i])
            else:
                minimum.append(minimum[-1])
        for i in range(len(minimum)-1,-1,-1):
            if nums[i]>minimum[i]:
                while stk and minimum[i]>=stk[-1]:
                    stk.pop()
                if stk and stk[-1]<nums[i] :
                    return True
                
                stk.append(nums[i])
        return False

      







        # ini=min(nums[:2])
        # j=max(nums[:2])
        # Flag=True
        # s=deque()
        # for i in range(2,len(nums)):
        #     if nums[i]<j and nums[i]>ini and Flag:
        #         return True
        #     if nums[i]>j:
        #         j=nums[i]
        #         Flag=True
        #     if nums[i]<ini:
        #         Flag=False
        #         ini=nums[i]
                  
        # return False




        # i = min(nums[:ind])
        # ind=nums.index(i)
        # if ind>=len(nums)-2:
        #     return False
        # for j in range(ind+1)
        # # j=max(nums)
        # # ind=nums.index(j)
        # # if ind==0 or ind==len(nums)-1:
        # #     return False
        # # i = min(nums[:ind])
        # # k=  max(nums[ind+1:])
        
        # # if i<k and k<j:
        # #     return True
        # # return False