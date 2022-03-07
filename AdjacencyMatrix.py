"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import ArrayList
import ArrayQueue
import ArrayStack


class AdjacencyMatrix(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = self.boolean_matrix(self.n)

    def boolean_matrix(self, n):
        return np.zeros([n,n],np.bool_)

    def boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i][j] = True
        #pass
        
    def remove_edge(self, i : int, j : int):
        # todo
        self.adj[i][j] = False
        #pass
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo
        return self.adj[i][j]
        #pass
        
    def out_edges(self, i) -> List:
        # todo
        l = ArrayList.ArrayList()
        for j in range(self.n):
            l.append(j)

        return l

        #pass

    def in_edges(self, j) -> List:
        # todo
        l = ArrayList.ArrayList()
        for i in range(self.n):

            if self.has_edge(i,j):
                l.append(i)

        return l
        #pass

    def bfs(self, r : int):
        # todo
        s = self.boolean_matrix(self.n)
        a_q = ArrayQueue.ArrayQueue()
        a_q.add(r)
        s[r] = True

        while a_q.size() > 0:
            i = a_q.remove()
            ngh = self.out_edges(i)

            for k in range(ngh.size()):
                j = ngh.get(k)

                if s[j] == False:
                    a_q.add(j)
                    s[j] = True
        #pass
    
    def dfs(self, r : int):
        # todo
        s = self.boolean_matrix(self.n)
        a_s = ArrayStack.ArrayStack()
        a_s.push(r)

        while a_s.size() > 0:
            i = a_s.pop()
            print(i, end='')
            s[i] = True
            ngh = self.out_edges(i)

            for j in range(ngh.size()):
                if s[ngh.get(j)] == False:
                    a_s.push(ngh.get(j))

                else:
                    continue
        #pass
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))

'''


