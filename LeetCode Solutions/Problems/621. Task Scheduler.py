class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        A = {}
        for i in tasks:
            if(i in A):
                A[i] += 1
            else:
                A[i] = 1
        A = sorted(A.values(), key = lambda x:-x)
        space = (A[0] -1) * n
        p = 0
        for i in range(1, len(A)):
            if(A[i] == A[0]):
                p += A[i]-1
            else:
                p += A[i]
        idle = max(0, space-p)
        return idle + len(tasks)