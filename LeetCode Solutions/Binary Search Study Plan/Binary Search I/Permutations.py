class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        factorial = 1
        for i in range (1, n+1):
            factorial = factorial * i
        ans = [nums]
        arr = nums
        for x in range(1, factorial):
            arr = [v for v in arr]
            i = len(arr)-1
            while(i>0):
                if(arr[i-1] < arr[i]):
                    break
                i = i-1
            i = i-1
            j = len(arr)-1
            while(j>i):
                if(arr[j] > arr[i]):
                    break
                j = j-1
            arr[i], arr[j] = arr[j], arr[i]  
            arr[i+1:] = sorted(arr[i+1:]) 
            ans.append([v for v in arr])
        return ans