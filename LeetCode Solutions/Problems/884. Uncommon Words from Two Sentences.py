class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst = s1.split()+s2.split()
        return [i for i in lst if lst.count(i)==1]