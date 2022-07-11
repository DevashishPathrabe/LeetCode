class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in "!?',;.":
            paragraph = paragraph.replace(i," ")
        x = Counter(paragraph.lower().split(" "))
        banned.append("")
        max_val = [0,""]
        for i in x:
            if i in banned :
                continue
            else:
                if max_val[0] < x[i]:
                    max_val[1] = i
                    max_val[0] = x[i]
        return max_val[1]