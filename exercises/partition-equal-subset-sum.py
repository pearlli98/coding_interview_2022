#https://leetcode.com/problems/partition-equal-subset-sum/solution/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # find sum of array elements
        total_sum = sum(nums)
        subset_sum = total_sum // 2
        
        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        
        # top down DP
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # return dfs(tuple(nums), len(nums) - 1, total_sum // 2)
    
        # bottom up DP
        memo = {}
        for i in range(total_sum // 2 + 1):
            memo[(0, i)] = False
        memo[(0, 0)] = True
            
        for i in range(1, len(nums)):
            for j in range(total_sum// 2 + 1):
                if nums[i] > j:
                    memo[(i, j)] = memo[(i - 1, j)]
                else:
                    memo[(i, j)] = memo[(i - 1, j)] or memo[(i - 1, j - nums[i])]
        
        return memo[(len(nums) - 1, total_sum // 2)]
    