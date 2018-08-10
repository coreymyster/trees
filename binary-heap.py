# Corey Sokol

from random import *

class BinaryHeap():
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
          if self.heap[i] < self.heap[i // 2]:
             tmp = self.heap[i // 2]
             self.heap[i // 2] = self.heap[i]
             self.heap[i] = tmp
          i = i // 2
                               
    
    def insert(self,item):
        self.heap.append(item)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def __repr__(self):
        return str(self.heap)

def main():
    alist = sample(range(1, 10), 9)
    heap = BinaryHeap()
    print("The random list is: ", alist)
    print("The current size of the heap is: ", heap)
    print("Begin adding items")
    
    # For testing purposes, visually shows each item added to the heap one by one
    # and prints the size each time.
    for i in alist:
        heap.insert(i)
        print(heap)
        print(heap.currentSize)
        
main()
