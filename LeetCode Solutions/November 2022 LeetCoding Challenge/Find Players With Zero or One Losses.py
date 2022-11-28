class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = {}
        answer1 = []
        answer2 = []
        result = [answer1, answer2]
        for match in matches:
            lose_count[match[0]] = 0
            lose_count[match[1]] = 0
        for match in matches:
            lose_count[match[1]] += 1   
        for player, lose in lose_count.items(): 
            if lose == 0:
                answer1.append(player)
            elif lose == 1:
                answer2.append(player) 
        answer1.sort()
        answer2.sort() 
        return result