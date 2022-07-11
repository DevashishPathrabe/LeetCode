class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash = {}
        for x in answers:
            if x not in hash:
                hash[x] = 0
            hash[x] += 1
        result = 0
        for x in hash:
            result += (math.ceil(hash[x] / (x + 1))) * (x + 1)
        return result