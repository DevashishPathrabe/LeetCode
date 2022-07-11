class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        currentlength = 0
        for i, ch in enumerate(s):
            if(ch.isdigit()):
                currentlength *= int(ch)
            else:
                currentlength += 1
            if(currentlength >= k):
                break
        k -= 1
        for j in range(i, -1, -1):
            if(s[j].isdigit()):
                currentlength //= int(s[j])
                k %= currentlength
            elif(currentlength == k + 1):
                return s[j]
            else:
                currentlength -= 1