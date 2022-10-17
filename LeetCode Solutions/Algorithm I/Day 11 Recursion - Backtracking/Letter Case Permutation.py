class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        L = [set([i.lower(), i.upper()]) for i in s]
        return map(''.join, itertools.product(*L))