# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

# binary check with conditions to check whether nums[mid] is beginning or end

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.binSearch(nums, target, True), self.binSearch(nums, target, False)]
        
        
    def binSearch(self, nums, target, isFirst):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                if isFirst:
                    if mid == low or (mid - 1 >= 0 and nums[mid - 1] < target):
                        return mid
                    high = mid - 1
                else:
                    if mid == high or (mid + 1 < len(nums) and nums[mid + 1] > target):
                        return mid
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
