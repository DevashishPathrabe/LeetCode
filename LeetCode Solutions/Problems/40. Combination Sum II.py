class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(nums, targetLeft, path):
            if targetLeft == 0:
                result.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] > targetLeft:
                    break
                helper(nums[i+1:], targetLeft-nums[i], path+[nums[i]])
        result = []
        helper(sorted(candidates), target, [])
        return result