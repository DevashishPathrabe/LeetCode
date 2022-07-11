class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        number = str(n)
        index = -1
        size = len(number)
        for i in range(1, size):
            if number[i] < number[i-1]:
                index = i
                while index > 0 and number[index] <= number[index-1]:
                    index-=1
                break
        if index == -1:
            return n
        return int(number[:index] + str(int(number[index]) - 1) + (size - index - 1) * '9')