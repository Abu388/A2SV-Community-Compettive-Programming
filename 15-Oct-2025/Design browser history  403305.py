# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class TrieNode:
    def __init__(self, val , next= None , prev =None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = TrieNode(homepage) 
        

    def visit(self, url: str) -> None:
        self.root.next = TrieNode( url,  prev = self.root)
        self.root = self.root.next
        

    def back(self, steps: int) -> str:

        while self.root.prev and steps > 0:
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:

        while self.root.next and steps > 0:
            self.root = self.root.next
            steps -= 1
        return self.root.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)