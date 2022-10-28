class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[1] for x in sorted([(heights[i], names[i]) for i in range(len(names))], reverse = True)]