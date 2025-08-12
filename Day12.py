class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        
        # Find max integer whose x-th power <= n
        max_num = 1
        while max_num**x <= n:
            max_num += 1
        max_num -= 1
        
        # dp[k][j] = ways to make sum k using numbers <= j
        dp = [[0] * (max_num + 1) for _ in range(n + 1)]
        
        # Base case: sum 0 can be made in exactly 1 way (choose nothing)
        for j in range(max_num + 1):
            dp[0][j] = 1
        
        for j in range(1, max_num + 1):
            power = j**x
            for k in range(1, n + 1):
                # Without j
                dp[k][j] = dp[k][j-1]
                # With j
                if k >= power:
                    dp[k][j] = (dp[k][j] + dp[k - power][j-1]) % MOD
        
        return dp[n][max_num]

s = Solution()
print(s.numberOfWays(10, 2))
print(s.numberOfWays(4, 1))