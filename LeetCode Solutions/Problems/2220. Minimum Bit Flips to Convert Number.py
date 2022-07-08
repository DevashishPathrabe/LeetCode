class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        if len(start_bin) < len(goal_bin):
            start_bin = ('0'*(len(goal_bin)-len(start_bin))) + start_bin
        if len(start_bin) > len(goal_bin):
            goal_bin = ('0'*(len(start_bin)-len(goal_bin))) + goal_bin
        count = 0
        for i in range(len(start_bin)):
            if start_bin[i] != goal_bin[i]:
                count += 1
        return count