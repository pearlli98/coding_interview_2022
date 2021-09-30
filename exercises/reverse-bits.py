question: https://leetcode.com/problems/reverse-bits/solution/

sol: bit by bit
i don't really understand the byte by byte, should come back later

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power #shift to the left by power bit, multiple by 2 ** power
            n = n >> 1 #shift to the right by 1 bit, divide by 2**1
            power -= 1
        return ret
