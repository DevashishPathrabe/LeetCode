class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if(n < 2):
            pass
        else:
            i = n -1
            while(i > 0):
                if(nums[i]> nums[i-1]):
                    temp = i - 1
                    break
                i -= 1
            if(i == 0):
                nums.reverse()
            else:
                swap = float('inf')
                for j in range(temp+1, n):
                    if(nums[j] > nums[temp]):                    
                        if(swap >= nums[j]):
                            swap =  nums[j]
                            justbigger = j
                nums[temp], nums[justbigger] = nums[justbigger], nums[temp]
                nums[temp+1:n]= reversed(nums[temp+1:n])