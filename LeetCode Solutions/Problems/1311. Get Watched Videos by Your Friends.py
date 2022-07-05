class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        A, V = set(friends[id]), set([id])
        for _ in range(level-1):
            A = set(sum([friends[a] for a in A],[])) - V - A
            V = V.union(A)
        C = collections.Counter(sorted(sum([watchedVideos[a] for a in A], [])))
        return sorted(C.keys(), key = lambda x: C[x])