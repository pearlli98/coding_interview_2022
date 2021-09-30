question: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        dp[i] is the largest sum of the subarray of A[i:]
        dp[i] = dp[i+1] + A[i], 
        
        """
        
        def sol1(nums):
            max_so_far = -math.inf
            max_ending_here = 0
            for i in nums:
                max_so_far = max(max_so_far, max_ending_here + i)
                max_ending_here = max(0, max_ending_here + i)
            return max_so_far
        
        def kadane(nums):
            if len(nums) == 0:
                return 0
            
            currentSubarray = maxSubarray = nums[0]
            for i in nums[1:]:
                currentSubarray = max(i, currentSubarray + i)
                maxSubarray = max(currentSubarray, maxSubarray)
            return maxSubarray
        
        return kadane(nums)
    
    
            
        
