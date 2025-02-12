# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        pairs = list(zip(names, heights))


        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        sorted_names = [name for name, _ in sorted_pairs]

        return (sorted_names)  