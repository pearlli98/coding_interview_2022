#https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]
        
        def partition(left, right, pivot):
            nums[pivot], nums[right] = nums[right], nums[pivot]
    
            cur = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[cur], nums[i] = nums[i], nums[cur]
                    cur += 1

            nums[right], nums[cur] = nums[cur], nums[right]
            return cur


        def findKSmallest(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left, right)
            pivot = partition(left, right, pivot_index)
            
            if k_smallest == pivot:
                return nums[k_smallest]

            elif k_smallest < pivot:
                return findKSmallest(left, pivot - 1, k_smallest)

            else:
                return findKSmallest(pivot + 1, right, k_smallest)
        
        return findKSmallest(0, len(nums) - 1, len(nums) - k)
        