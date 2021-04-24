class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        masks = defaultdict(list)
        for word in wordList:
            for i, ch in enumerate(word):
                masks[word[:i] + '*' + word[i+1:]].append(word)
        steps = 1
        queue = [beginWord]
        while(queue):
            nextQueue = []
            while(queue):
                currentWord = queue.pop()
                if(currentWord == endWord):
                    return steps
                for i, ch in enumerate(currentWord):
                    mask = currentWord[:i] + '*' + currentWord[i+1:]
                    nextQueue.extend(masks[mask])
                    del masks[mask]
            steps += 1
            queue = nextQueue
        return 0