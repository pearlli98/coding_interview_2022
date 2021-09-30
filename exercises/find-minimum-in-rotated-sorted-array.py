question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Sol: binary search

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        def foundMin(mid):
            if mid == 0 and nums[mid + 1] > nums[mid] and nums[-1] > nums[mid]:
                return True
            elif mid == len(nums) - 1 and nums[mid - 1] > nums[mid] and nums[0] > nums[mid]:
                return True
            elif mid > 0 and mid < len(nums) and nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                return True
            return False
        
        left = 0
        right = len(nums) - 1
        
        if nums[left] < nums[right]:
            return nums[left]
        
        
        while left <= right:
            mid = int((left + right) / 2.0)
            if foundMin(mid):
                return nums[mid]
            #如果想要用这个条件往左/右缩小范围的话，就得assume存在rotation
            #所以需要在while前面加一个if filter out没有rotation的情况
            elif nums[0] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
            
