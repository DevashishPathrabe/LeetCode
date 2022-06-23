class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        diffsum = 0
        start = 0
        for i in range(n):
            tank += gas[i]-cost[i]
            diffsum += gas[i]-cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        if start < n and diffsum >= 0:
            return start
        else:
            return -1