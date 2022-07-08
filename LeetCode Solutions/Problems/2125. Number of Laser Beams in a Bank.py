class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, laserBeams = 0, 0
        for s in bank:
            count = s.count('1')
            if count == 0:
                continue
            laserBeams += prev * count
            prev = count
        return laserBeams