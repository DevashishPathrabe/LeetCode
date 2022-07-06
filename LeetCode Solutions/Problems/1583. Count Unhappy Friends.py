class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if n == 2:
            return 0
        hash = {}
        unhappy = 0
        for i in pairs:
            hash[i[0]] = i[1]
            hash[i[1]] = i[0]
        for i in range(len(preferences)):
            pairedwith = hash[i]
            temp = preferences[i][:preferences[i].index(pairedwith)]
            if len(temp) == 0:
                continue
            for j in temp:
                if preferences[j].index(i) < preferences[j].index(hash[j]):
                    unhappy += 1
                    break
        return unhappy