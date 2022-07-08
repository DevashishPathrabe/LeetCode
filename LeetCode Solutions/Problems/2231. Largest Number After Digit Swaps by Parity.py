class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int, str(num))) 
        evens = sorted([d for d in num if not d%2])
        odds = sorted([d for d in num if d%2])
        return ''.join(str(odds.pop() if d%2 else evens.pop()) for d in num)