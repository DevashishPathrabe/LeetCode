class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        g = defaultdict(set)
        seen = [0] * numCourses
        for i,j in prerequisites:
            g[i].add(j)
        def hasCycle(s):
            if seen[s] == 1:
                return False
            if seen[s] == -1:
                return True
            seen[s] =- 1
            res = any(hasCycle(t) for t in g[s])
            if res:
                return True
            ans.append(s)
            seen[s] = 1
            return False
        return [] if any(hasCycle(s) for s in range(numCourses)) else ans