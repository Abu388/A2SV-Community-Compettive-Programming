# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.heap = []
        
        self.count = 0
    def addNum(self, num: int) -> None:
        bisect.insort(self.heap , num)
        
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.heap[self.count // 2] + self.heap[(self.count // 2) - 1]) / 2
        else:
            return self.heap[self.count // 2]



        # if self.count % 2 == 0:
        #     late = []
        #     for _ in range(self.count// 2):
        #         pre = heappop(self.heap)
        #         late.append(pre)
        #     val = heappop(self.heap)
        #     heappush(self.heap , val)
        #     for i in late:
        #         heappush(self.heap , i)
        #     return (pre + val) / 2
        # else:
        #     late = []
        #     for _ in range((self.count// 2)):
        #         late.append(heappop(self.heap))
        #     val = heappop(self.heap)
        #     heappush(self.heap , val)
        #     for i in late:
        #         heappush(self.heap , i)
        #     return val
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()