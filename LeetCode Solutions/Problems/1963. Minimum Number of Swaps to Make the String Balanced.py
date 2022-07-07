class Solution:
    def minSwaps(self, s: str) -> int:
        counter = 0
        minimumNumberOfSwaps = 0
        for i in s:
            if i == ']':
                if counter == 0:
                    minimumNumberOfSwaps += 1
                    counter += 1
                else:
                    counter -= 1
            else:
                counter += 1
        return minimumNumberOfSwaps