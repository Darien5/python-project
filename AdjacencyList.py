"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def boolean_matrix(self, n):
        return np.zeros([n,n],np.bool_)

    def boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i].append(j)

        #pass

    def remove_edge(self, i : int, j : int):
        # todo
        for k in range(len(self.adj[i]) - 1):

            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)

        #pass
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo
        for k in range(self.adj[i].size()):

            if self.adj[i].get(k) == j:
                return True
        #pass
        
    def out_edges(self, i) -> List:
        # todo
        return self.adj[i]
        #pass

    def in_edges(self, i) -> List:
        # todo
        output = ArrayList.ArrayList()

        for j in range(self.n):

            if self.has_edge(j,i):
                output.append(j)

        return output
        #pass
    
    def bfs(self, r : int):
        # todo
        s = self.boolean_array(self.n)
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
                    s[j] = True #Double Check and experiment!
        #pass

    def dfs(self, r : int):
        # todo
        s = self.boolean_array(self.n)
        a_s = ArrayStack.ArrayStack()
        a_s.push(r)

        while a_s.size() > 0:
            i = a_s.pop()
            print(i,end='')
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


    def bfs2(self, r : int, s : int):
        s_ = self.boolean_array(self.n)
        a_q = ArrayQueue.ArrayQueue()
        l = []
        a_q.add(r)
        l.append(r)
        s_[r] = True
        d = 0

        while a_q.size() > 0 and d < s:
            i = a_q.remove()
            ngh = self.out_edges(i)

            for k in range(ngh.size()):
                j = ngh.get(k)

                if s_[j] == False:
                    a_q.add(j)
                    l.append(j)
                    s_[j] = True

            d += 1

        return l

    def dfs2(self, r1 : int, r2 : int):
        s = self.boolean_array(self.n)
        d = np.zeros(self.n)
        a_s = ArrayStack.ArrayStack()
        d[r1] = 0
        a_s.push(r1)

        while a_s.size() > 0:
            i = a_s.pop()
            s[i] = True
            ngh = self.out_edges(i)

            for k in range(ngh.size()):
                j = ngh.get(k)

                if s[j] == False:
                    a_s.push(j)
                    d[j] = d[i] + 1

                if j == r2:
                    return d[j]

        return -1