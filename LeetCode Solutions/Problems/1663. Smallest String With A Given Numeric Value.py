class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        numericValue = '_bcdefghijklmnopqrstuvwxy_'
        lexicographicallySmallestString = 'z' * (k // 25)
        if(k % 25):
            lexicographicallySmallestString = numericValue[k%25] + lexicographicallySmallestString
        return 'a' * (n - len(lexicographicallySmallestString)) + lexicographicallySmallestString