question: https://leetcode.com/problems/alien-dictionary/

sol1: generate graph + topo sort

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(set)
        inDegree = Counter({letter: 0 for word in words for letter in word})
        
        for first, second in zip(words[:-1], words[1:]):
            for f, s in zip(first, second):
                if f != s:
                    if s not in adjList[f]:
                        adjList[f].add(s)
                        inDegree[s] += 1
                    break
            else:
                if len(second) < len(first): return ""
                    
        output = []
        queue = deque([letter for letter in inDegree if inDegree[letter] == 0])
        while queue:
            cur = queue.popleft() #bfs, first in first out
            output.append(cur) 
            for i in adjList[cur]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)
        
        if len(output) != len(inDegree):
            return ""
        return ''.join(output)
                    
                    
        
