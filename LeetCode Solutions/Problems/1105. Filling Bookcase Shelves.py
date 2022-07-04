class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0]
        for i in range(len(books)):
            currentWidth = books[i][0]
            j = i - 1
            maxHeight = books[i][1]
            height = dp[i] + books[i][1]
            while j >= 0 and currentWidth + books[j][0] <= shelfWidth:
                currentWidth += books[j][0]
                maxHeight = max(maxHeight, books[j][1])
                height = min(height, dp[j] + maxHeight)
                j -= 1
            dp.append(min(height, dp[i] + books[i][1]))    
        return dp[-1]