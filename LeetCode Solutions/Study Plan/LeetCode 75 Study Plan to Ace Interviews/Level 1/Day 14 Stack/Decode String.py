class Solution:
    def decodeString(self, s: str) -> str:
        decodedString = ''
        for i in range(len(s)):
            if(s[i] != ']'):
                decodedString += s[i]
            else:
                f, n = '', ''
                while(decodedString and decodedString[-1] != '['):
                    f, decodedString = decodedString[-1]+f, decodedString[:-1]
                decodedString = decodedString[:-1]
                while(decodedString and decodedString[-1] in '0123456789'):
                    n, decodedString = decodedString[-1]+n, decodedString[:-1]
                decodedString += f*int(n)
        return decodedString