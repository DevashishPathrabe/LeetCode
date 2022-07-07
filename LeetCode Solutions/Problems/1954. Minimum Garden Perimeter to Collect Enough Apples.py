class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        i, summ, current = 0, 0, 0
        while True:
            current = 3 * i * i
            summ += 4 * current
            if summ >= neededApples:
                return i*4*2
            i += 1