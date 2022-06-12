class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(not nums):
            return []
        temp = ''
        smallestSortedList = []
        for i in range(len(nums)-1):
            if(not temp):
                temp += str(nums[i])
                if(nums[i+1]-nums[i] != 1):
                    smallestSortedList.append(temp)
                    temp = ''
            else:
                if(nums[i+1]-nums[i] != 1):
                    temp += '->'+str(nums[i])
                    smallestSortedList.append(temp)
                    temp = ''
        if(temp):
            temp += '->'+str(nums[-1])
            smallestSortedList.append(temp)
        else:
            smallestSortedList.append(str(nums[-1]))
        return smallestSortedList