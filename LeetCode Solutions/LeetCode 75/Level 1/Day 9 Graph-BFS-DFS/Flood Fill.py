class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def recursion(image, row, column, color):
            if (row < 0 or row >= len(image) or column < 0 or column >= len(image[0])):
                return
            elif (image[row][column] != color):
                return
            else:
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                image[row][column] = -1
                for r, c in directions:
                    recursion(image, row+r, column+c, color)
                image[row][column] = newColor
                return image
        return recursion(image, sr, sc, image[sr][sc])