#Python program to print topological sorting of a DAG
from collections import defaultdict
from typing import OrderedDict

# given a list of tuple (A, B) representing that B refers A inside a company
# output list of employees sorted by the number of people they directly or indirectly refer
# and break tie with names, (A, None) means no one refers A


class Graph:
    def __init__(self, super):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = set() #No. of vertices
        self.children = set()
        self.num_children = OrderedDict()
        self.super = super
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        if v == 'None':
            self.V.add(u)
            return
        self.graph[u].append(v)
        self.V.update([u, v])
        self.children.add(v)
 
    def addSuperNode(self):
        heads = self.V.difference(self.children)
        self.graph[self.super] = list(heads)
        
    def get_children(self, v):
        if len(self.graph[v]) == 0:
            self.num_children[0] = self.num_children.get(0, []) + [v]
            return set()
        else:
            res = set()
            for i in self.graph[v]:
                res.update(self.get_children(i))
            res.update(self.graph[v])
            l = len(res)
            self.num_children[l] = self.num_children.get(l, []) + [v]
            return res
    
    def get_order(self):
        g.addSuperNode()
        self.get_children(self.super)
        print(self.graph)
        res = []
        for i in list(self.num_children.keys())[::-1]:
            res += sorted(list(set(self.num_children[i])))
        return res[1:]

 
g = Graph('super')
g.addEdge('Alice', 'Noah')
g.addEdge('Noah', 'Kyle')
g.addEdge('Noah', 'Amy')
g.addEdge('Noah', 'Jay')
g.addEdge('Amy', 'Pearl')
g.addEdge('P', 'None')

print(g.get_order())