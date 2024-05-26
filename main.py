MOD = 10**9 + 7

class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3  # "P", "L", "A"
        
        # DP table
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # Base case
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            for a in range(2):
                for l in range(3):
                    # Add 'P'
                    dp[i][a][0] = (dp[i][a][0] + dp[i-1][a][l]) % MOD
                    
                    # Add 'A'
                    if a > 0:
                        dp[i][a][0] = (dp[i][a][0] + dp[i-1][a-1][l]) % MOD
                    
                    # Add 'L'
                    if l > 0:
                        dp[i][a][l] = (dp[i][a][l] + dp[i-1][a][l-1]) % MOD
        
        # Sum up all valid states of length n
        result = 0
        for a in range(2):
            for l in range(3):
                result = (result + dp[n][a][l]) % MOD
        
        return result

