class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentMap, answer = defaultdict(list), []
        for pathsString in paths:
            seperation = pathsString.split(" ")
            for i in range(1, len(seperation)):
                parts = seperation[i].split('(')
                content = parts[1][:-1]
                contentMap[content].append(seperation[0] + '/' + parts[0])
        for j in contentMap.values():
            if(len(j) > 1):
                answer.append(j)
        return answer