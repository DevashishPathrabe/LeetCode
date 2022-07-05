class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices%2 == 1:
            return []
        if ((tomatoSlices - 2 * cheeseSlices) / 2) < 0 or ((4 * cheeseSlices - tomatoSlices) / 2) < 0:
            return []
        return [(tomatoSlices - 2 * cheeseSlices) // 2, (4 * cheeseSlices - tomatoSlices) // 2]