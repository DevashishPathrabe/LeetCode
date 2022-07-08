class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = {}
        ans1 = []
        ans2 = []
        result = [ans1, ans2]
        for match in matches:
            lose_count[match[0]] = 0
            lose_count[match[1]] = 0
        for match in matches:
            lose_count[match[1]] += 1   
        for player, lose in lose_count.items(): 
            if(lose == 0):
                ans1.append(player)
            elif(lose == 1):
                ans2.append(player) 
        ans1.sort()
        ans2.sort() 
        return result