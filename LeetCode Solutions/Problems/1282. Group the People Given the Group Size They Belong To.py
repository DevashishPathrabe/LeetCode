class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        resultList = []
        for i in range(0,len(groupSizes)):
            if groupSizes[i] not in dict:
                dict[groupSizes[i]] = [i]
            else:
                dict[groupSizes[i]] += [i]
        for k,v in dict.items():
            for i in range(0,len(v),k):
                resultList.append(v[i:i+k])
        return resultList