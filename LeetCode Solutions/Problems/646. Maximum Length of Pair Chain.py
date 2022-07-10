class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[0])
        pairs.sort(key = lambda x:x[1])
        chain = 1
        i = 1
        while i < len(pairs):
            if pairs[i-1][1] < pairs[i][0]:
                chain += 1
                i += 1
            else:
                pairs.pop(i)
        return chain