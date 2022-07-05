class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        dic = {}
        result = []
        for numerator in range(1, n):
            for denominator in range(numerator+1, n+1):
                x = numerator / denominator
                if x not in dic:
                    dic[x] = 1
                    result.append(str(numerator) + '/' + str(denominator))
        return result