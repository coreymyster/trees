# Corey Sokol

from random import *

# Creates the BinaryHeap
class BinaryHeap():
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0
    
    # Organizes the list passed in and percolates larger values down into the tree
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    # Identifies the minimum child and returns the value of the child
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
     
    # Build the heap from a random list passed in 
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    
    # For display purposes to make it easier to read objects of the BinaryHeap class
    def __repr__(self):
        return str(self.heap)
            
def main():
    
    # Generates a random list of numbers to pass to buildHeap()
    alist = sample(range(1, 10), 9)
    print("The random list is: ", alist)
    
    # Passes the randomized list to buildHeap()
    heap = BinaryHeap()
    heap.buildHeap(alist)
    
    print("The built heap is: ", heap)
        
main()
    