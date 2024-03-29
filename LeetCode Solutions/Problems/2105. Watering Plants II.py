class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        Alice , Bob  = capacityA, capacityB
        result, i, j = 0, 0, len(plants)-1
        while i < j:
            if Alice >= plants[i]:
                Alice -= plants[i]
            else:
                result += 1
                Alice = capacityA - plants[i]
            if Bob >= plants[j]:
                Bob -= plants[j]
            else:
                result += 1
                Bob = capacityB - plants[j]
            i += 1    
            j -= 1
        if i == j and Alice < plants[i] and Bob < plants[i]:
            return result + 1
        else:
            return result