class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        noOfDifferentTransformations = set()
        for word in words:
            current = ""
            for char in word:
                current += codes[ord(char)-97]
            noOfDifferentTransformations.add(current)
        return len(noOfDifferentTransformations)