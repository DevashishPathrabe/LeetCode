class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        visited, level, ln = {start}, [start], 0
        while level:
            new_level = []
            for item in level:
                if item == end:
                    return ln
                for i in range(len(item)):
                    for j in ['A', 'C', 'G', 'T']:
                        mutations = item[:i] + j + item[i + 1:]
                        if mutations not in visited and mutations in bank:
                            visited.add(mutations)
                            new_level.append(mutations)
            level = new_level
            ln += 1
        return -1