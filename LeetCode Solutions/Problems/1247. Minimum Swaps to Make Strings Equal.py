class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counter1, counter2 = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    counter1 += 1
                else:
                    counter2 += 1
        if counter1 % 2 == 0 and counter2 % 2 == 0:
            return (counter1 + counter2) // 2
        elif counter1 % 2 == 1 and counter2 % 2 == 1:
            return counter1//2 + counter2//2 + 2
        return -1