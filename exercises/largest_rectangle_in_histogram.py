#https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights):
        S = [0]
        max_area = 0
        for i in range(1, len(heights)):
            if heights[i] >= heights[S[-1]]:
                S.append(i)
            else:
                while S and heights[S[-1]] > heights[i]:
                    cur_height = heights[S.pop()]
                    width = i if not S else (i - S[-1] - 1)
                    max_area = max(max_area, cur_height * width)
                S.append(i)
    
        while S:
            cur_height = heights[S.pop()]
            width = len(heights) if not S else (len(heights) - S[-1] - 1)
            max_area = max(max_area, cur_height * width) 
        
        return max_area
                    
        