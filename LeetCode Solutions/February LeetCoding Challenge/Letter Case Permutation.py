class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        L = [set([i.lower(), i.upper()]) for i in S]
        return map(''.join, itertools.product(*L))