class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = Node()
            n = n.children[c]
        n.is_word = True

    def search(self, word: str) -> bool:
        def helper(w, n):
            if not w:
                return n.is_word
            if w[0] != '.':
                if w[0] not in n.children:
                    return False
                return helper(w[1:], n.children[w[0]])
            else:
                return any([helper(w[1:], n.children[x]) for x in n.children])
        return helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)