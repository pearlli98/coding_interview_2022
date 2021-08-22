#题目：https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        if len(digits) == 0:
            return ''
        
        def helper(index, path):
            if len(path) == len(digits):
                com.append(''.join(path))
                return
            for i in d[digits[index]]:
                path.append(i)
                helper(index + 1, path)
                path.pop()
            
        com = []
        helper(0, [])
        
        return com
    

