class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        friends = [val for val in range(1, n+1)]
        while len(friends) > 1:
            if index + k - 1 >= n:
                index  = (index + k - 1) % n
            else:
                index  = index + k - 1
            friends.pop(index)
            n -= 1
        return friends[0]