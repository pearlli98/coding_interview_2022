question: https://leetcode.com/problems/number-of-1-bits/
sol 1: count every 1-bit
sol 2: n & (n-1) to count all 1-bits 

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        mask = 1
        
        for i in range(32):
            if n & mask != 0:
                bits += 1
                
            mask <<= 1
            
        return bits
        
