question: https://leetcode.com/problems/longest-increasing-subsequence/solution/

sol 1: traditional bottom up dp
sol 2: build a subsequence (a little bit counterintuitive bc the subsequence built is not always the correct one, just the correct length)
sol 3: optimize sol 2 with binary search

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)

