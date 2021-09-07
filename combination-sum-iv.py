question: https://leetcode.com/problems/combination-sum-iv/submissions/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # top down
        # dp = {0:1}
        # def recurse(n):
        #     if n not in dp:
        #         dp[n] = sum([recurse(n - j) for j in nums if n - j >= 0])   
        #     return dp[n]
        # return recurse(target)
        
        
        # bottom up
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]
