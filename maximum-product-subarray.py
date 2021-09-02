question: https://leetcode.com/problems/maximum-product-subarray/submissions/

sol: dp? not really, need to keep track of max and min in order to cope with negative values

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsofar = minsofar = maxoverall = nums[0]
        
        for i in nums[1:]:
            tmp = max(maxsofar * i, minsofar * i, i)
            minsofar = min(maxsofar * i, minsofar * i, i)
            maxsofar = tmp
            maxoverall = max(maxoverall, maxsofar)
        
        return maxoverall
        
        
        
        
