# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUCache:
    def __init__(self, capacity: int):
        self.arr = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.arr:
            value=self.arr[key]
            del self.arr[key]
            self.arr[key]=value
            return value
      
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.arr:
            del self.arr[key]  
        elif len(self.arr) >= self.capacity:
            for i in self.arr:
                del self.arr[i]
                break
        self.arr[key] = value 


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.arr = []
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         for i, (k, v) in enumerate(self.arr):
#             if k == key:
#                 self.arr.pop(i)  
#                 self.arr.append([k, v])  
#                 return v
#         return -1

#     def put(self, key: int, value: int) -> None:
#         for i, (k, v) in enumerate(self.arr):
#             if k == key:
#                 self.arr.pop(i) 
#                 self.arr.append([key, value])  
#                 return
        
#         if len(self.arr) >= self.capacity:
#             self.arr.pop(0) 
        
#         self.arr.append([key, value])  












# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)