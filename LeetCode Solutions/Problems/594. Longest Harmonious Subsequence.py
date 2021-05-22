class Solution:
    def findLHS(self, nums: List[int]) -> int:
        temp = Counter(nums)
        keys = temp.keys()
        difference = 0
        for i in keys:
            if(i-1 in keys):
                if(temp[i-1] + temp[i] > difference):
                    difference = temp[i-1] + temp[i]
        return difference