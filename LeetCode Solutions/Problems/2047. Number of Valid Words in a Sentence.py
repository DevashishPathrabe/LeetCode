class Solution:
    def countValidWords(self, sentence: str) -> int:
        return len(list(filter(lambda x: re.match('^[a-z]*([a-z]-[a-z])?[a-z]*[!\.,]?$', x), sentence.split())))