# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q=deque(range(len(deck)))
        res=[0]*len(deck)
        deck.sort()
        for i in deck:
            n=q.popleft()
            res[n]=i
            if q:
                q.append(q.popleft())


        return res
        