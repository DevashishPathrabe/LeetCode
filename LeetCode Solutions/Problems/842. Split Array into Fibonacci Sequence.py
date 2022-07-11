class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        L, T, t = len(num), "", []
        for i in range(1, L-2):
        	for j in range(1, L-i-1):
        		if (i > 1 and num[0] == '0') or (j > 1 and num[i] == '0'): continue
        		a, b = int(num[:i]), int(num[i:i+j])
        		T, t = num[:i+j], [a,b]
        		while len(T) < L:
        			c = a + b
        			T += str(c)
        			t += [c]
        			a, b = b, c
        		if len(T) == L and T == num and len(t) > 2 and t[-1] < 2**31 - 1: return t
        return []