class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, str(n)))
        length = len(nums)

        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:

                prv = float('inf')
                next_ind = -1

                for j in range(i + 1, length):
                    if nums[j] > nums[i] and nums[j] < prv:
                        prv = nums[j]
                        next_ind = j

                nums[i], nums[next_ind] = nums[next_ind], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])

                result = int("".join(map(str, nums)))
                return result if result < 2**31 else -1

        return -1