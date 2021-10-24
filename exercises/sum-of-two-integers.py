# question:https://leetcode.com/problems/sum-of-two-integers/solution/

# sol: bitwise operations 
# x Xor y is sum of two binary without carry and diff of two binary without borrow
# carry is x and y shifted to left
# borrow is (not x) and y shifted to left

class Solution(object):
    def getSum(self, a, b):
        
        x, y = abs(a), abs(b)
        
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1
        
        
        if a * b >= 0:
            while y:
                x, y = x ^ y, (x & y) << 1
                
        else:
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return sign * x
            
        
        
