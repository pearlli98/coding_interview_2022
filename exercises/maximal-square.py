# https://leetcode.com/problems/maximal-square/submissions/

# sol: DP[i][j] = length of maximum square that ends at (i, j)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for i in range(C+1)] for j in range(R+1)]
        max_area = 0
        for i in range(1, R+1):
            for j in range(1, C+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_area = max(max_area, dp[i][j] ** 2)
                else:
                    dp[i][j] = 0
        print(dp)
        return max_area
