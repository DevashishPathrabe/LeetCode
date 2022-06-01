class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        dp = {}
        arr = [int(x) for x in str(n)]
        def helper(position, flag, zero):
            if position > len(arr):
                return 0
            if position == len(arr):
                return 1
            key = (position, flag, zero)
            if key in dp:
                return dp[key]
            if flag == True:
                limit  = 9
            else:
                limit = arr[position]
            ans = 0
            if zero == True and position != len(arr)-1:
                ans+= helper(position+1, True, True)
            for i in digits:
                if int(i) <= limit:
                    ans += helper(position+1, True if int(i) < arr[position] else flag, False)
            dp[key] = ans
            return ans
        return helper(0, False, True)