class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        ad = defaultdict(list)
        for i, n in enumerate(arr):
            ad[n].append(i)
        ans = [0] * len(arr)
        dq = deque([len(arr) - 1])
        while dq:
            i = dq.popleft()
            if i < len(arr) - 1 and ans[i + 1] == 0 and i + 1 < len(arr) - 1:
                ans[i + 1] = ans[i] + 1
                dq.append(i + 1)
            if i > 0 and ans[i - 1] == 0:
                ans[i - 1] = ans[i] + 1
                if i - 1 == 0:
                    return ans[0]
                dq.append(i - 1)
            for j in ad[arr[i]]:
                if ans[j] == 0 and j < len(arr) - 1:
                    ans[j] = ans[i] + 1
                    if j == 0:
                        return ans[0]
                    dq.append(j)
            ad.pop(arr[i])