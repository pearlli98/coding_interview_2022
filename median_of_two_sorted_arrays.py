import math

#题目：https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
#解1：binary search找合并后array的左半边的最后一个数
# https://atharayil.medium.com/median-of-two-sorted-arrays-day-36-python-fcbd2dbbb668
#解2: 找两个array的第k个数
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2496/Concise-JAVA-solution-based-on-Binary-Search

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        def merge(nums1, nums2):
            # merge array O(m+n)
            L = nums1
            R = nums2

            arr = []
            i = j = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr.append(L[i])
                    i += 1
                else:
                    arr.append(R[j])
                    j += 1

            # Checking if any element was left
            while i < len(L):
                arr.append(L[i])
                i += 1

            while j < len(R):
                arr.append(R[j])
                j += 1

            Len = len(nums1) + len(nums2)

            if Len % 2 != 0:
                return arr[Len / 2]
            else:
                return (arr[Len/2] + arr[Len/2 - 1]) / 2.0
        
        def hi(nums1, nums2):
            array_1 = nums1
            array_2 = nums2
            start = 0
            end = len(array_1)
            X = len(array_1)
            Y = len(array_2)
            while(start <= end):

                partitionX = int((start + end )/2)
                partitionY = int((X + Y + 1 )/2 - partitionX)

                #Edge case when there is nothing on the left side, then we assign x1 to infinity
                if(partitionX == 0):
                    X1 = float('-inf')
                else:
                    X1 = array_1[partitionX - 1]

                if(partitionX == len(array_1) ):
                    X2 = float('inf')
                else:
                    X2 = array_1[partitionX]

                if(partitionY == 0):
                    Y1 = float('-inf')
                else:
                    Y1 = array_2[partitionY - 1]

                if(partitionY == len(array_2) ):
                    Y2 = float('inf')
                else:
                    Y2 = array_2[partitionY]
                
                if((X1 <= Y2) and (Y1 <= X2)):

                    # We have found correct partitions

                    #Check if the sum of length of both is odd or even
                    if( (X+Y) % 2 == 0):

                        median = ((max(X1,Y1) + min(X2, Y2))/2.0)
                        return median
                    else:

                        median = max(X1,Y1)
                        return median

                elif(Y1 > X2):
                    start = partitionX + 1
                else:
                    end = partitionX - 1
        
        def getkth(a, a_start, b, b_start, k):
            print(a[a_start:], b[b_start:], k)
            if a_start > len(a) - 1:
                return b[b_start + k - 1]
            if b_start > len(b) - 1:
                return a[a_start + k - 1]
            if k == 1:
                return min(a[a_start], b[b_start])
            
            amid, bmid = float('inf'), float('inf')
            if a_start + k/2 - 1 < len(a): amid = a[a_start + k/2 - 1]
            if b_start + k/2 - 1 < len(b): bmid = b[b_start + k/2 - 1]
            
            # if amid == float('inf') or bmid == float('inf'):
            
            if amid < bmid:
                return getkth(a, a_start + k/2, b, b_start, k - k/2)
            else:
                return getkth(a, a_start, b, b_start + k/2, k - k/2)
            
        l = (len(nums1) + len(nums2) + 1) / 2
        r = (len(nums1) + len(nums2) + 2) / 2
                   
        return (getkth(nums1, 0, nums2, 0, l) + getkth(nums1, 0, nums2, 0, r)) / 2.0

#当其中一个array剩下少于k/2个element时，直接assume略长的array的前k/2不含有median，为什么呢
# 不可能含有，因为假设含有的话，两个array的长度并不够k！（左边是少于k/2，右边刚好k/2）



