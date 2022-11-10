class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        curlen = 0
        for i, ch in enumerate(S):
            if(ch.isdigit()):
                curlen *= int(ch)
            else:
                curlen += 1
            if(curlen >= K):
                break
        K -= 1
        for j in range(i, -1, -1):
            if(S[j].isdigit()):
                curlen //= int(S[j])
                K %= curlen
            elif(curlen == K + 1):
                return S[j]
            else:
                curlen -= 1