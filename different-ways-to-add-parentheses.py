question: https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/

sol: recursion +  memoization! 

class Solution:
    def __init__(self):
        self.memo = {}
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        result = []
        for i in range(len(expression)):
            c = expression[i]
            if c == '+' or c == '-' or c == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                result += [self.calc(l, r, c) for l in left for r in right]
        if len(result) == 0:
            result.append(int(expression))
        self.memo[expression] = result
        return result
    
    def calc(self, left, right, c):
        if c == '+':
            return left + right
        elif c == '*':
            return left * right
        elif c == '-':
            return left - right
        
