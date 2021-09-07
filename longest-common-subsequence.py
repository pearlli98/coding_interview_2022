quesiton: https://leetcode.com/problems/longest-common-subsequence/solution/

sol1: dp bottom up, base case a little tricky

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #dp[i][j] = longest common subseq for text1[:i] and text2[:j]
        dp = [[0 for i in text2] for j in text1]
        
        if text1[0] == text2[0]:
            dp[0][0] = 1
        
        for i in range(1, len(text1)):
            if text1[i] == text2[0] or dp[i-1][0] == 1:
                dp[i][0] = 1
        
        for i in range(1, len(text2)):
            if text2[i] == text1[0] or dp[0][i-1] == 1:
                dp[0][i] = 1
                
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
        
        return dp[len(text1) - 1][len(text2) - 1]
        
