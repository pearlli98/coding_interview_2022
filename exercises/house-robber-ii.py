quesiton: https://leetcode.com/problems/house-robber-ii/submissions/

sol: use house robber 1 (O(n)) but find the max of rob(A[:L-1]) and rob(A[1:L])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.linear_rob(nums[:len(nums) - 1]), self.linear_rob(nums[1:len(nums)]))
    
    def linear_rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        
        return dp[len(nums) - 1]
