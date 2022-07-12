class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @lru_cache(None)
        def connect(w1, w2):
            return [w2[i:] for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]
        N = len(words) 
        dp = [[(float("inf"), "")] * N for _ in range(1<<N)]
        for i in range(N): dp[1<<i][i] = (len(words[i]), words[i])
        for mask in range(1<<N):
            n_z_bits = [j for j in range(N) if mask & 1<<j]
            for j, k in permutations(n_z_bits, 2):
                cand = dp[mask ^ 1<<j][k][1] + connect(words[k], words[j])
                dp[mask][j] = min(dp[mask][j], (len(cand), cand))
        return min(dp[-1])[1]