class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        List = []
        for s in words:
            even = ""
            odd = ""
            for i in range(len(s)):
                if i%2 != 0:
                    odd += s[i]
                else:
                    even += s[i]
            odd = ''.join(sorted(odd))
            even = ''.join(sorted(even))
            List.append(str(odd) + str(even))
        return len(set(List))