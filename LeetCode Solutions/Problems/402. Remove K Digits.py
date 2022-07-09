class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if (len(num) == k):
            return "0"
        i = 0
        while (k != 0):
            try:
                if (int(num[i]) > int(num[i+1])):
                    num = str(int(num[:i] + num[i+1:]))
                    k -= 1
                    if (i != 0):
                        i = i-1
                    else:
                        i = 0
                else:
                    i += 1
            except:
                break
        return num if k == 0 else num[:-k] if num[:-k] != "" else "0"