class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        k = 1
        for i in range(len(target)):
            while target[i] > k:
                result.append("Push")
                result.append("Pop")
                k += 1
            result.append("Push")
            k += 1
        return result