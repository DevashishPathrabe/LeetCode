class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        result = []
        for i in range(len(favoriteCompanies)):
            s = set(favoriteCompanies[i])
            flag = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if s.issubset(set(favoriteCompanies[j])):
                    flag = False
                    break
            if flag:
                result += [i]
        return result