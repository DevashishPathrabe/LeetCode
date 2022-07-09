class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity == jug2Capacity:
            return targetCapacity == jug1Capacity
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False
        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0