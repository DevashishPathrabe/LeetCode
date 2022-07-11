class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if target == 0:
            return len(position)
        if n == 0:
            return 0
        time = [float(target - position) / speed for position, speed in sorted(zip(position, speed))]
        result = current = 0
        for t in time[::-1]:
            if t > current:
                result += 1
                current = t
        return result