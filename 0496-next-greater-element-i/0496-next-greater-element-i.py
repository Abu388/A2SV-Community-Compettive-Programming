class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = defaultdict(int)
        stk = []
        for num in nums2:
            if not stk:
                stk.append(num)
            else:
                while stk and stk[-1] < num:
                    mp[stk.pop()] = num
                stk.append(num)
        for i in range(len(nums1)):
            if nums1[i] not in mp:
                nums1[i] = -1
            else:
                nums1[i] = mp[nums1[i]]
        return nums1

