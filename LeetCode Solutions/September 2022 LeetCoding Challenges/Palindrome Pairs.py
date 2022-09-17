class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        for x in range(len(words)):
            d[words[x]] = x
        l = []
        dp = set()
        for x in range(len(words)):
            q = words[x]
            if q == '':
                continue
            if q == q[::-1] and '' in d:
                if (d[q],d['']) not in dp or (d[''],d[q]) not in dp:
                    l.append([d[q], d['']])
                    l.append([d[''], d[q]])
                    dp.add((d[q], d['']))
                    dp.add((d[''], d[q]))
            for y in range(len(q)):
                t = q[:y]
                if t[::-1] in d and (q+t[::-1])[::-1] == (q+t[::-1]) and d[q] != d[t[::-1]]:
                    if (d[q], d[t[::-1]]) not in dp:
                        l.append([d[q], d[t[::-1]]])
                        dp.add((d[q], d[t[::-1]]))
                t1 = q[-y+1:]
                if t1[::-1] in d and (t1[::-1]+q)[::-1] == (t1[::-1]+q) and d[t1[::-1]] != d[q]:
                    if (d[t1[::-1]], d[q]) not in dp:
                        l.append([d[t1[::-1]], d[q]])
                        dp.add((d[t1[::-1]], d[q]))
        return l