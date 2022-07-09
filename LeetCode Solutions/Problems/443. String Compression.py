class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        if len(chars) <= 1:
            return len(chars)
        i = 0
        while i < len(chars):
            count = 1
            while (i < len(chars) - 1 and chars[i] == chars[i + 1]):
                count += 1
                i += 1
            if count > 1:
                s += chars[i]
                s += str(count)
            else:
                s += chars[i]
            i += 1
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)