class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, currentLine, numLetters = [], [], 0
        for w in words:
            if len(currentLine) + numLetters + len(w) > maxWidth:
                for i in range(maxWidth - numLetters):
                    currentLine[i  % (len(currentLine) - 1 or 1)] += ' '
                result.append(''.join(currentLine))
                currentLine, numLetters = [], 0
            currentLine += [w]
            numLetters += len(w)
        return result + [' '.join(currentLine).ljust(maxWidth)]