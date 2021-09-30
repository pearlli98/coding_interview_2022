problem: https://leetcode.com/problems/graph-valid-tree/solution/

sol1: have a parent map and make sure all children aren't parent; at the end, check that all nodes have been visited

sol2: 
1. for a graph to be a tree, it has to have exactly n - 1 edges
2. then check with dfs if all nodes can be reached starting from one node

Compare to sol1, this first check for num of edges, if that satisfies, then
a. if the all nodes are connected, there has to be no cycles; 
b. if not fully connected, has to have cycles

#sol1

class Solution:
    def __init__(self):
        self.adjList = defaultdict(set)
        self.parent = defaultdict(int)
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        for a, b in edges:
            self.adjList[a].add(b)
            self.adjList[b].add(a)
        if self.dfs() and len(self.parent) == n:
            return True
        return False
    
    def dfs(self):
        agenda = [0]
        self.parent[0] = -1
        while agenda:
            cur = agenda.pop()
            for i in self.adjList[cur]:
                # if we have already seen neighbor, must contain a cycle
                if i in self.parent:
                    return False
                # remove opposite edge
                if cur in self.adjList[i]:
                    self.adjList[i].remove(cur)
                agenda.append(i)
                self.parent[i] = cur
        return True
        
#sol2
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)
    
    return len(seen) == n
