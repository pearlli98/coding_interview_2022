Quesiton: https://leetcode.com/problems/consecutive-numbers-sum/
Sol: Math!!!

class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        counter = 0
        k = 1.0
        while k <= (2*n + 0.25) ** 0.5 - 0.5:
            if float(float(n) / k - (k+1)/2.0).is_integer():
                counter += 1
            k += 1.0
            
        return counter
        
