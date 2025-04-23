# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = []
        pre = numCourses - 1
        ind = [0]*(numCourses)
        print(ind)
        for u , v in prerequisites:
            graph[v].append(u)
            ind[u] += 1
        q = deque(i for i in range(numCourses) if ind[i] == 0)
        while q:
            node = q.popleft()
            
            res.append(node)

            for i in graph[node]:

                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        if len(res) != len(ind):
            return []
        return res
        