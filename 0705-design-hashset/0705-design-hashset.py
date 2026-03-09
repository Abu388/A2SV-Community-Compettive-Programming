class MyHashSet:

    def __init__(self):
        # Boolean array to store keys from 0 to 10^6
        self.size = 10**6 + 1
        self.data = [False] * self.size

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]