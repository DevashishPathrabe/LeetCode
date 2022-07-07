class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        result = maxLength = 0
        for length, width in rectangles:
            squareLength = min(length, width)
            if squareLength > maxLength:
                result = 1
                maxLength = squareLength
            elif squareLength == maxLength:
                result += 1
        return result