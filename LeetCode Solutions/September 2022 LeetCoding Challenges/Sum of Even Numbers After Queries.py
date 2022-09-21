class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sumeven = sum(i for i in nums if i%2==0)
        for i in queries:
            nums[i[1]] += i[0]
            if (i[0]%2 == 0 and nums[i[1]]%2 == 0):
                sumeven += i[0]
            elif (i[0]%2 == 1 and nums[i[1]]%2 == 0):
                sumeven += nums[i[1]]
            elif (i[0]%2 == 1 and nums[i[1]]%2 == 1):
                sumeven -= (nums[i[1]]-i[0])
            answer.append(sumeven)
        return answer