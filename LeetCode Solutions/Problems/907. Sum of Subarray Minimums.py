class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        total = 0
        stack = [-1]
        MOD = 10**9 + 7
        for i in range(len(arr)):
            while len(stack) > 1 and arr[stack[-1]] > arr[i]:
                last = stack.pop()
                total += (last-stack[-1]) * (i-last) * arr[last] % MOD
            stack.append(i)
        return total % MOD