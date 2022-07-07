class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birthYears = sorted([i[0] for i in logs])
        maxPopulation, earliestYear = 0, 0
        for year in birthYears:
            population = 0
            for dates in logs:
                if dates[0] <= year and dates[1] > year:
                    population += 1
            if population > maxPopulation:
                earliestYear = year
                maxPopulation = population
        return earliestYear