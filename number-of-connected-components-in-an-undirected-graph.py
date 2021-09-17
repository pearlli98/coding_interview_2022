problem: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/solution/

sol1: dfs
sol2: disjoint union set (quite smart and intuitive but slower)

class Solution:
    def __init__(self):
        self.visited = set()
        self.neighbors = defaultdict(set)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = set()
        for edge in edges:
            a, b = edge
            nodes.update(edge)
            self.neighbors[a].add(b)
            self.neighbors[b].add(a)
        counter = 0
        for node in range(n):
            if node in self.visited:
                continue
            self.dfs(node)
            counter += 1
        return counter
        
        
    def dfs(self, start):
        agenda = [start]
        while agenda:
            cur = agenda.pop()
            if cur in self.visited:
                continue
            for i in self.neighbors[cur]:
                agenda.append(i)
            self.visited.add(cur)
        return 
        
        
        
