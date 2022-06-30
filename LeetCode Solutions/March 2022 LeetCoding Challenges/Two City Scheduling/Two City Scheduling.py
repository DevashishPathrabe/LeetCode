class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda k : k[0] - k[1])
        n = len(costs) // 2   
        return sum([costs[i][0] + costs[i+n][1] for i in range(n)])