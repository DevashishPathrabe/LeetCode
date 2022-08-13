class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = sum(chalk)
        ans = k%chalk_sum
        for i in range(len(chalk)):
            if ans == 0 or ans < chalk[i]:
                return i
            ans -= chalk[i]