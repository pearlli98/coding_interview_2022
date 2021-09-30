question: https://leetcode.com/problems/integer-break/submissions/

sol: memoization and dp
dp[i] = max(dp[j] * dp[k]) such that j + k = i
https://medium.com/@gepphkat/dynamic-programming-343-integer-break-4aa8dde3ee0f

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0: 0, 1: 1, 2: 1, 3: 2}
        if n in memo:
            return memo[n]
        
        for i in range(4, n + 1):
            curMax = -1
            for j in range(2, i / 2 + 1):
                left = j
                right = i - j
                maxLeft = max(left, memo[left])
                maxRight = max(right, memo[right])
                curMax = max(curMax, maxLeft * maxRight)
            memo[i] = curMax
        
        return memo[n]
        
