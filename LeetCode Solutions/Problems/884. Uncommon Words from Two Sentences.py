class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        List = s1.split() + s2.split()
        return [i for i in List if List.count(i) == 1]