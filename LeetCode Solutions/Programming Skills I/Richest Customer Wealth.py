class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts.sort(key=sum)
        return sum(accounts[-1])