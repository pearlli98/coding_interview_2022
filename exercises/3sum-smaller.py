question: https://leetcode.com/problems/3sum-smaller/solution/

sol: two pointer

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        for i in range(0, len(nums) - 2):
            res += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return res
        
        
    def twoSumSmaller(self, nums, start, target):
        res = 0
        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res
        
