class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i, j = 0, 0
        count, result = 0, 0
        while j < len(arr):
            count += arr[j]
            if (j - i + 1) == k:
                if (count / k) >= threshold:
                    result += 1
                count -= arr[i]
                i += 1
                j += 1
            elif (j - i + 1) < k:
                j += 1
        return (result)