class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        tuples = 0
        counter = {}
        for a in A:
            for b in B:
                counter[a+b] = counter.get(a+b, 0) + 1
        for c in C:
            for d in D:
                tuples += counter.get(-c-d, 0)
        return tuples