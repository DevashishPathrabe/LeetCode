class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            for root in dictionary:
                n = len(root)
                if(word[:n] == root):
                    sentence[i] = root
                    break
        return " ".join(sentence)