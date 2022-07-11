class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        length = len(s)
        i = 0
        lines = 1
        pixels = 0
        while i < length:
            if pixels + widths[ord(s[i])-97] > 100:
                lines += 1
                pixels = widths[ord(s[i])-97]
            else:
                pixels += widths[ord(s[i])-97]
            i += 1
        return [lines, pixels]