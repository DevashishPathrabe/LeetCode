class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            isFlower = flowerbed[i]
            if not isFlower:
                condition = isFlower
                if i > 0:
                    condition = condition or flowerbed[i-1] 
                if i < len(flowerbed) - 1:
                    condition = condition or flowerbed[i+1]
                if not condition:
                    count += 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        return count >= n