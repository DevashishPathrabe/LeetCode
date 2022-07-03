class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n, available=len(tops), []
        for no in range(1, 7):
            c = 0
            for i in range(n):
                if (tops[i] == no or bottoms[i] == no):
                    c += 1
            if (c == n):
                available.append(no)
        if (not(len(available))):
            return -1
        ans = []
        for no in available:
            fir, sec = 0, 0
            for i in range(n):
                if (tops[i] == no):
                    fir += 1
            for i in range(n):
                if (bottoms[i] == no):
                    sec += 1        
            fir = n - fir
            sec = n - sec
            ans.append(min(fir, sec))         
        return min(ans)