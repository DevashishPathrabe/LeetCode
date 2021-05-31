class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, 1
        length = 0
        while(right < len(arr)):
            if(arr[left] >= arr[right]):
                left += 1
                right += 1
            else:
                haveRight = 0
                while(right < (len(arr)-1) and arr[right] < arr[right+1]):
                    right += 1
                while(right < (len(arr)-1) and arr[right] > arr[right+1]):
                    right += 1
                    haveRight = 1
                if(haveRight):
                    length = max(length,right-left+1)
                left = right
                right = left + 1
        return length