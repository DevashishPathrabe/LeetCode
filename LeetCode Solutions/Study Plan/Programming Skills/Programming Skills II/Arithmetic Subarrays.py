class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result_list = [False]*len(l)
        for i in range(len(l)):
            sub_list = nums[l[i]:r[i]+1]
            sub_list.sort()
            diff_list = [sub_list[i] - sub_list[i-1] for i in range(1, len(sub_list))]
            result_list[i] = diff_list.count(diff_list[0]) == len(diff_list)
        return result_list