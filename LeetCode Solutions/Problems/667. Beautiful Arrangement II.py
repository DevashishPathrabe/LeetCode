class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer, a, z = [0]*n, 1, k+1
        for i in range(k+1):
            if(i%2):
                answer[i] = z
                z -= 1
            else:
                answer[i] = a
                a += 1
        for i in range(k+1, n):
            answer[i] = i+1
        return answer