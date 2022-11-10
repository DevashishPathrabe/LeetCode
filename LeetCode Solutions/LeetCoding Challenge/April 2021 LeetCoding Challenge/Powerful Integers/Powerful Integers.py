class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        listOfPowerfullIntegers, xi = set(), 1
        while (xi < bound):
            yj = 1
            while (xi + yj <= bound):
                listOfPowerfullIntegers.add(xi + yj)
                if (y == 1):
                    break
                yj *= y
            if (x == 1):
                break
            xi *= x
        return list(listOfPowerfullIntegers)