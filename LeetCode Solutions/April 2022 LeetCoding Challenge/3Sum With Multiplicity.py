class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        nmap, third, tuples = [0 for _ in range(101)], ceil(target / 3) - 1, 0
        for num in arr:
            nmap[num] += 1
        for k in range(min(target,100), third, -1):
            rem = target - k
            half = ceil(rem / 2) - 1
            for j in range(min(rem, k), half, -1):
                i = rem - j
                x, y, z = nmap[i], nmap[j], nmap[k]
                if(i == k):
                    tuples += x * (x-1) * (x-2) // 6
                elif(i == j):
                    tuples += x * (x-1) // 2 * z
                elif(j == k):
                    tuples += x * y * (y-1) // 2
                else:
                    tuples += x * y * z
        return tuples % 1000000007