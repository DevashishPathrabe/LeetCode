class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = []
        def per(depth):
            if depth == len(arr) - 1:
                res.append(arr[:])
            for i in range(depth, len(arr)):
                arr[i], arr[depth] = arr[depth], arr[i]
                per(depth+1)
                arr[i], arr[depth] = arr[depth], arr[i]
        per(0)
        re = ""
        for i in res:
            if i[0] * 10 + i[1] < 24 and i[2] * 10 + i[3] < 60:
                re = max(re, str(i[0]) + str(i[1])+':' + str(i[2]) + str(i[3]))
        return re