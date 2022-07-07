class Solution:
    def totalMoney(self, n: int) -> int:
        div, rem = n // 7, n % 7
        return 28 * div + rem * (rem + 1) // 2 + div * (div - 1) // 2 * 7 + div * rem