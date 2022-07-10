class MagicDictionary:

    def __init__(self):
        self.dic = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dic += dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.dic:
            if len(searchWord) == len(word):
                count = 0
                for i in range(len(searchWord)):
                    if searchWord[i] != word[i]:
                        count += 1
                if count == 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)