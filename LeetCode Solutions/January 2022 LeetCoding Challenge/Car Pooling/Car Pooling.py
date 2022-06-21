class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = 1001*[0]
        for trip in trips:
            car[trip[1]] += trip[0]
            car[trip[2]] -= trip[0]
        passengers = 0
        for p in car:
            passengers += p
            if passengers > capacity:
                return False
        return True