class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        x = int(math.sqrt(area))
        while x > 0:
        	if area % x == 0:
        		return [area//x, x]
        	else:
        		x -= 1