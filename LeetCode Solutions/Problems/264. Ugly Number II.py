class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyList = [1]
        uglyHeap = [(2, 2, 0), (3, 3, 0), (5, 5, 0)]
        while n > 1:
            nextUgly, factor, index = heapq.heappop(uglyHeap)
            if nextUgly != uglyList[-1]:
                uglyList.append(nextUgly)
                n -= 1
            index += 1
            heapq.heappush(uglyHeap, (factor * uglyList[index], factor, index))
        return uglyList[-1]