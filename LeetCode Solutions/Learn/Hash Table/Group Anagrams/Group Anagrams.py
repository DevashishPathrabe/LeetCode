class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if (key not in groups):
                groups[key] = [s]
            else:
                groups[key].append(s)
        return groups.values()