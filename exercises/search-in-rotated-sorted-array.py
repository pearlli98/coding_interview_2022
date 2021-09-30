question: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

Sol: binary search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = int((left + right) / 2.0)
            cur = nums[mid]
            if cur == target:
                return mid
            else:
                if cur > target:
                    if cur < nums[0]:
                        right = mid - 1
                    elif target < nums[0]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else: 
                    #这个>=好tricky。。。
                    #wrong cases试出来的，not sure why
                    if cur >= nums[0]:
                        left = mid + 1
                    elif target >= nums[0]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1
