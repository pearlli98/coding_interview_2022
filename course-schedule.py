question: https://leetcode.com/problems/course-schedule/

check whether graph is DAG
sol 1: DFS (check backedge)
sol 2: topo sort

from collections import defaultdict

class Node(object):
    def __init__(self):
        self.out = []
        self.inDegree = 0

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        #sol 1: dfs
        def dfs():
            d = defaultdict(list)

            for course, prev in prerequisites:
                d[prev].append(course)

            path = set()
            visited = set()

            def isCyclic(course):

                if course in visited:
                    return False
                if course in path:
                    return True

                path.add(course)
                backedge = False

                for child in d[course]:
                    if isCyclic(child):
                        backedge = True
                        break

                path.remove(course)
                visited.add(course)

                return backedge

            for i in range(numCourses):
                if isCyclic(i):
                    return False
            return True
    
        #sol 2: topo sort 
        def topo():
            L = []
            d = defaultdict(Node)
            
            totalEdges = 0
            for course, prev in prerequisites:
                d[prev].out.append(course)
                d[course].inDegree += 1
                totalEdges += 1
            
            endNodes = []
            for i, node in d.items():
                if node.inDegree == 0:
                    endNodes.append(i)
            
            removedEdges = 0
            while endNodes:
                course = endNodes.pop(0)
                for child in d[course].out:
                    d[child].inDegree -= 1
                    removedEdges += 1
                    if d[child].inDegree == 0:
                        endNodes.append(child)
                        
            # print(removedEdges, totalEdges)
            if removedEdges == totalEdges:
                return True
            return False
                    
                
        return topo()
            
