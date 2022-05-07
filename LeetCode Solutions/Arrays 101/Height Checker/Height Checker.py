class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        array = sorted(heights)
        numberOfStudents = 0
        for i in range(len(array)):
            if (array[i] != heights[i]):
                numberOfStudents += 1
        return numberOfStudents