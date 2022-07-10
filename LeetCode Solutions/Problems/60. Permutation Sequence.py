class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        permutationSequence = ''
        while n>1:
            temp = math.factorial(n-1)
            position = (k-1) // temp
            k = k % temp
            m = nums[position]
            permutationSequence += str(m)
            nums.remove(m)
            n -= 1
        return permutationSequence + str(nums[-1])