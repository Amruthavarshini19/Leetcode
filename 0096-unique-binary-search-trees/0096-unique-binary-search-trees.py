class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for nodes in range(2,n+1):
            for root in range(1,nodes+1):
                l = root-1
                r = nodes-root
                dp[nodes]+=dp[l]*dp[r]
        return dp[n]
        