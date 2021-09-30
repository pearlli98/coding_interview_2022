question: https://leetcode.com/problems/reverse-integer/submissions/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # print(-2**31, -2 ** 31 / 10)
        rev = 0
        if x < 0:
            return -1 * self.reverse(abs(x))
        while x != 0:
            pop = x % 10
            x = int(x / 10)
            if rev > 2**31/10 or (rev == 2**31/10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        return rev
    
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1 * self.reverse2(abs(x))
    
        s = int(str(x)[::-1])
        
        if s > 2**31 - 1:
            return 0
            
        return s
            
        
