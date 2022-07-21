class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length, duplicatedNumber = len(nums), 0
        seen, sumOfnums = [0]*(length+1), length * (length+1) // 2
        for num in nums:
            sumOfnums -= num
            if(seen[num]):
                duplicatedNumber = num
            seen[num] += 1
        return [duplicatedNumber, sumOfnums + duplicatedNumber]