class Solution(object):
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            window_sum = 0
            for j in range(k + 1):
                window_sum += dp[j]
                if j >= i:
                    window_sum -= dp[j - i]
                window_sum %= MOD
                new_dp[j] = window_sum
            dp = new_dp
        return dp[k]
        