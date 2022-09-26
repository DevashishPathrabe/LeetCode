class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        root = [i for i in range(26)]
        idx = lambda x: ord(x) - ord('a')
        for x, s, _, y in equations:
            if s == '=':
                root[find(idx(x))] = find(idx(y))
        for x, s, _, y in equations:
            if s == '!' and find(idx(x)) == find(idx(y)):
                return False
        return True