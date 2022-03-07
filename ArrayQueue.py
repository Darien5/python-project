import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(1,2*self.n))
        b[0:self.n] = self.a[0:self.n]

        self.a = b
        #pass


    
    def add(self, x : np.object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if self.n + 1 > len(self.a): self.resize()
        self.a[(self.j +self.n) % len(self.a)] = x

        self.n += 1
        #pass

    def remove(self) -> np.object :
        '''
            remove the first element in the queue
        '''
        if self.n <= 0: raise Exception
        x = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1

        if len(self.a) >= self.n * 3: self.resize()

        return x

        #pass

    def size(self) :
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x