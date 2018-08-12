# Corey Sokol

from random import *

# Creates the BinaryHeap
class BinaryHeap():
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0
    
    # When a new item is added the percUp function checks if the parent is less than the new
    # element. If so, then they swap places.
    def percUp(self,i):
        while i // 2 > 0:
          if self.heap[i] < self.heap[i // 2]:
             tmp = self.heap[i // 2]
             self.heap[i // 2] = self.heap[i]
             self.heap[i] = tmp
          i = i // 2
                               
    # Adds a new item and calls the percUp function to see if the item needs to move up the tree
    def insert(self,item):
        self.heap.append(item)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    # For display purposes to make it easier to read objects of the BinaryHeap class
    def __repr__(self):
        return str(self.heap)

def main():
    # Creates a random list of integers
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
