class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(char):
            i = 0
            count = 0
            maximum = 0
            for j in range(len(answerKey)):
                if answerKey[j] == char:
                    count += 1
                while i <= j and count > k:
                    if answerKey[i] == char:
                        count -= 1
                    i += 1
                maximum = max(maximum, j-i+1)
            return maximum
        return max(helper("T"), helper("F"))