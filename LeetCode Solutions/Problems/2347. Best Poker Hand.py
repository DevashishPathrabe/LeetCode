class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if (len(set(suits)) == 1):
            return "Flush"
        hm = {}
        for element in ranks:
            if (element not in hm):
                hm[element] = 1
            else:
                hm[element] += 1
        list1 = list(hm.values())
        for element in list1:
            if (element >= 3):
                return "Three of a Kind"
        for element in list1:
            if (element >= 2):
                return "Pair"
        return "High Card"