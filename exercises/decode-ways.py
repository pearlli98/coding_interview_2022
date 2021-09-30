question: https://leetcode.com/problems/decode-ways/submissions/

sol:
dp[i] = number of ways to decode s[:i]
just like climbing stairs, dp[i] = dp[i-1] + dp[i-2] but need to check whether the strings are valid

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != 0 else 0
        
        for i in range(2, len(s) + 1):
            # single string
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            #  double digit
            num = int(s[i-2:i])
            if num >= 10 and num <= 26:
                dp[i] += dp[i - 2]
        
        return dp[len(s)]
           

