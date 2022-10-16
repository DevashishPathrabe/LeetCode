class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def generator(num):
            if len(num) == n:
                ans.append(int("".join(num)))
                return
            i = int(num[-1])
            if k == 0:
                generator(num + [str(i)])
            else:
                if ((i - k) >= 0):
                    generator(num + [str(i-k)])
                if ((i + k) <= 9):
                    generator(num + [str(i+k)])
        for i in range(1,10):
            generator([str(i)])
        return ans