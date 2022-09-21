from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        arr = defaultdict(int)
        for i in words:
            arr[i] += 1
        count = 0
        maximum = 0
        odd = True
        for i in words:
            if  arr[i] != 0 and arr[i[::-1]] != 0 and i != i[::-1]:
                count += (min(arr[i], arr[i[::-1]])*4)
                arr[i] = 0
                arr[i[::-1]] = 0
            else:
                if i == i[::-1]:
                    if arr[i]%2 == 0:
                        count += (arr[i]*2)
                    else:
                        odd = False
                        count += ((arr[i]-1)*2)
                    arr[i] = 0
        if odd == False:
            count += 2
        return count