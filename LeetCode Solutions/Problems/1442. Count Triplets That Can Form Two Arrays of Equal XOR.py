class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        List = defaultdict(list)
        n = len(arr)
        List[0].append(-1)
        numberOfTriplets = 0
        x = 0
        for i in range(n):
            x ^= arr[i]
            if x in List:
                for j in List[x]:
                    numberOfTriplets += (i-j)-1
            List[x].append(i)
        return numberOfTriplets