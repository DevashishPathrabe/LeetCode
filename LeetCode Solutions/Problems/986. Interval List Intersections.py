class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        M, N = len(firstList), len(secondList)
        i, j = 0, 0
        final = []
        while i < M and j < N:
            iStart, iEnd = firstList[i]
            jStart, jEnd = secondList[j]
            if jEnd < iStart:
                j += 1
                continue
            elif iEnd < jStart:
                i += 1
                continue
            finalStart = max(iStart, jStart)
            finalEnd = min(iEnd, jEnd)
            final.append([finalStart, finalEnd])
            if iEnd <= jEnd:
                i += 1
            else:
                j += 1
        return final