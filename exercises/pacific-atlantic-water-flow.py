problem: https://leetcode.com/problems/pacific-atlantic-water-flow/solution/

sol1: bfs from all bordering cells

class Solution:
    def __init__(self):
        self.map = None
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.map = heights
        R, C = len(heights), len(heights[0])
        self.R, self.C = R, C
        pacific_border = [(0, i) for i in range(C)] + [(i, 0) for i in range(1, R)]
        atlantic_border = [(R - 1, i) for i in range(C)] + [(i, C - 1) for i in range(R - 1)]
        return self.intersection(self.bfs(pacific_border), self.bfs(atlantic_border))
    
    def bfs(self, agenda):
        visited = set()
        while agenda:
            cur = agenda.pop(0)
            if cur in visited:
                continue
            for i in self.getHigherNeighbors(cur):
                agenda.append(i)
            visited.add(cur)
        return visited
    
    def getHigherNeighbors(self, cell):
        cell_r, cell_c = cell
        return [(r, c) for r, c in [(cell_r - 1, cell_c), (cell_r + 1, cell_c), (cell_r, cell_c - 1), (cell_r, cell_c + 1)] if self.withinBorder(r, c) and self.map[r][c] >= self.map[cell_r][cell_c]]
    
    def withinBorder(self, r, c):
        return r >= 0 and c >= 0 and r < self.R and c < self.C
    
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
