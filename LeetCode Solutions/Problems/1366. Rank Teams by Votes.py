class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = defaultdict(lambda : [0]*len(votes[0]))
        for vote in votes:
            for p, t in enumerate(vote):
                dic[t][p] -= 1
        result = dict(sorted(dic.items(), key=lambda x: (x[1], x[0])))
        return ''.join(result.keys())