class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        orig, lcase, mask = set(wordlist), defaultdict(), defaultdict()
        regex = r'[aeiou]'
        for i in range(len(wordlist)-1,-1,-1):
            word = wordlist[i]
            wlow = word.lower()
            lcase[wlow] = word
            mask[re.sub(regex, '*', wlow)] = word
        for i in range(len(queries)):
            query = queries[i]
            qlow = query.lower()
            qmask = re.sub(regex, '*', qlow)
            if (query in orig):
                continue
            elif (qlow in lcase):
                queries[i] = lcase[qlow]
            elif (qmask in mask):
                queries[i] = mask[qmask]
            else:
                queries[i] = ""
        return queries