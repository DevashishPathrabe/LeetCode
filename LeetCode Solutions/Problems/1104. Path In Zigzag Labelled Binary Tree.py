class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        l = 1
        while label > 2**l-1:
            l += 1
        i = label - 2**(l-1)
        if l % 2 == 0:
            i = 2**(l-1)-1-i
        result = []
        for j in range(l,0,-1):
            if j % 2:
                result.append(2**(j-1)+i)
            else:
                result.append((2**j-1)-i)
            i //= 2
        return reversed(result)