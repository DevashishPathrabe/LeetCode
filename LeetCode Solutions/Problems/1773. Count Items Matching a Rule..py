class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        searchIndex = 2
        if(ruleKey == "type"):
            searchIndex = 0
        elif(ruleKey == "color"):
            searchIndex = 1
        matchedItemsCount = 0
        for i in range(len(items)):
            if(items[i][searchIndex] == ruleValue):
                matchedItemsCount += 1
        return matchedItemsCount