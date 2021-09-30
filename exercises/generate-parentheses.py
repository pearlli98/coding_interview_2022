#https://leetcode.com/problems/generate-parentheses/submissions/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # backtracking        
                        
        def backtrack(path, l, r):
            if len(path) == 2 * n:
                com.add(''.join(path))
                return
            if l < n:
                path.append('(')
                backtrack(path, l+1, r)
                path.pop()
            if r < l:
                path.append(')')
                backtrack(path, l, r+1)
                path.pop()
            
        com = set()
        backtrack([], 0, 0)
        return list(com)
