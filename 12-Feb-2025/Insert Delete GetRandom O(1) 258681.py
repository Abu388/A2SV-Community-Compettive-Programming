# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet(object):

    def __init__(self):
        self.has = {}
        self.arr = []

    def insert(self, val):
        if val in self.has:
            return False
        self.has[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        if val not in self.has:
            return False
        ind = self.has[val]
        last = self.arr[-1]
        self.arr[ind] = last
        self.has[last] = ind
        self.arr.pop()
        del self.has[val]
        return True

    def getRandom(self):
        return random.choice(self.arr)
