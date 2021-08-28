题目：https://leetcode.com/problems/3sum/
Sol：Hashset

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        trip = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # iterate through each number only once 
            if i != 0 and nums[i-1] == nums[i]:
                continue
            res = self.twoSum(nums[i+1:], -1 * nums[i])
            if res:
                # print(nums[i], res)
                trip += [[nums[i]] + j for j in res]
        return trip
        
       
    def twoSum(self, nums, target):
        table = {}
        pairs = []
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in table:
                pairs.append([nums[i], complement])
                # after you got a pair, skip until a new number appears 
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
            table[nums[i]] = True
            i += 1
            
        return pairs
        
