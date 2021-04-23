class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        frequency = defaultdict(int)
        for row in wall:
            rowSum = row[0]
            for i in range(1, len(row)):
                frequency[rowSum] += 1
                rowSum += row[i]
        return len(wall) - max(frequency.values() or [0])