class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        rank = [0] * len(s)
        for x, y in pairs:
            self.union(x, y, rank, parent)
        graph = defaultdict(list)
        for node in range(len(s)):
            graph[self.find_parent(node, parent)].append(node)
        result = [""] * len(s)
        for node in graph:
            children = graph[node]
            children_to_char = sorted(s[i] for i in children)
            for idx, char in zip(children, children_to_char):
                result[idx] = char
        return "".join(result)
    def find_parent(self, node, parent):
        if node == parent[node]:
            return node
        parent[node] = self.find_parent(parent[node], parent)
        return parent[node]
    def union(self, node1, node2, rank, parent):
        par1 = self.find_parent(node1, parent)
        par2 = self.find_parent(node2, parent)
        if rank[par1] < rank[par2]:
            parent[par1] = par2
        elif rank[par1] > rank[par2]:
            parent[par2] = par1
        else:
            parent[par1] = par2
            rank[par2] += 1