class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        charOcc_dict = Counter(s)
        visited = set()
        result = ["0"]
        for char in s:
            charOcc_dict[char] -= 1
            if char in visited:
                continue
            lastChar = result[-1]
            while (char < lastChar) and charOcc_dict.get(lastChar, None) > 0:
                result.pop()
                visited.discard( lastChar )
                lastChar = result[-1]
            result.append( char )
            visited.add( char )
        return ''.join(result[1:])