class Solution:
    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return '1'
        previous = '1'
        result = ''
        count = 1
        for i in range(n-1):
            result = ''
            for j in range(len(previous)):
                if (j == len(previous)-1 or previous[j] != previous[j+1]):
                    result += str(count) + previous[j]
                    count = 1
                else:
                    count += 1
            previous = result
        return result