class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashmap = {
            ' ': ' '
        }
        i = 97
        for c in key:
            if c not in hashmap:
                hashmap[c] = chr(i)
                i += 1
        decodedMessage = ''
        for c in message:
            decodedMessage += hashmap[c]
        return decodedMessage