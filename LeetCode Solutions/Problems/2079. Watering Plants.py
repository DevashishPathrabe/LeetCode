class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        numberOfSteps = 0
        current = capacity 
        for i in range(n):
            numberOfSteps += 1
            if plants[i] > current:
                numberOfSteps += i + i 
                current = capacity - plants[i]
            else:
                current = current - plants[i]
        return numberOfSteps