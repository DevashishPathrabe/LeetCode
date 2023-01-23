class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def helper(node: int):
            count = Counter()
            if node not in seen:
                count[labels[node]] += 1 
                seen.add(node)
                for child in g.get(node, []):
                    count += helper(child)
                result[node] = count[labels[node]]
            return count
        g, result, seen = defaultdict(list), [0] * n, set()
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        helper(0)
        return result