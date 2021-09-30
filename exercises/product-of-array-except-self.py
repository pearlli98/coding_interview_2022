question: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        def sol1(nums):

            if 0 in nums:
                if nums.count(0) > 1:
                    return [0] * len(nums)

                else:
                    res = [0] * len(nums)
                    i = nums.index(0)
                    prod = 1
                    for num in nums[:i] + nums[i+1:]:
                        prod *= num
                    res[i] = prod
                    return res

            else:
                prod = 1
                for num in nums:
                    prod *= num
                return [prod/i for i in nums]
        
        
        def sol2(nums):
            
            l = len(nums)
            L, R = [1] * l, [1] * l
            
            for i in range(l):
                if i - 1 >= 0:
                    L[i] = nums[i-1] * L[i-1]
                    
            for i in range(l-1, -1, -1):
                if i + 1 < l:
                    R[i] = nums[i+1] * R[i+1]
            
            return [i*j for i, j in zip(L, R)]
        
        return sol2(nums)
