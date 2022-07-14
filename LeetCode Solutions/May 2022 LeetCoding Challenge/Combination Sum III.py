class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def helper(target, start, path):
            lengthPath = len(path)
            if target < 0 or lengthPath > k:
                return
            if lengthPath == k and target == 0:
                result.append(path)
                return
            for i in range(start, 10):
                helper(target - i, i + 1, path + [i])
        helper(n, 1, [])
        return result