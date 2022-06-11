class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque()
        for i in num:
            while k > 0 and q and q[-1] > i:
                k -=1
                q.pop()
            q.append(i)
        ans = ''.join(q).lstrip('0')
        if k > 0:
            ans = ans[:-k]
        return ans if len(ans) != 0 else '0'