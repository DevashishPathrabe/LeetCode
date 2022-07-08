class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while True:
            for i, count in enumerate(tickets):
                if count:
                    count -= 1
                    tickets[i] = count
                    time += 1
                if i == k and tickets[i] == 0:
                    return time