#!/bin/usr/env python3

from random import sample
from time import time
import P2
import heapq

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged

class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        PriorityQueue.__init__(self, max_size)
        
    def put(self,val):
    # put should take in a value val and insert it at the end of the elements list.
    # This method should raise an IndexError if called after max_size is reached. Nothing should be returned.
        if len(self) < self.max_size:
            elements = self.elements
            elements.append(val)
            self.elements = elements
        else:
            raise IndexError('Queue is already at maximum length, cannot put another element.')
    
    def get(self):
    # get should remove the smallest value from elements and return it.
    # raise an IndexError if called on an empty priority queue
        if len(self)>0:
            elements = self.elements
            min_elem = min(elements)
            elements.remove(min_elem)
            self.elements = elements
            return(min_elem)
        else:
            raise IndexError('Queue is empty, cannot perform get on an empty queue.')
            
    
    def peek(self):
    # peek should return the smallest value in the queue.
    # raise an IndexError if called on an empty priority queue
        if len(self)>0:
            elements = self.elements
            min_elem = min(elements)
            return(min_elem)
        else:
            raise IndexError('Queue is empty, cannot perform peek from an empty queue.')

class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        PriorityQueue.__init__(self, max_size)
        
    def put(self, val):
    # put should push the element to the heap (heappush)
    # raise an IndexError if called after max_size is reached. Nothing should be returned
        if len(self)<self.max_size:
            minheap = P2.MinHeap(self.elements)
            minheap.heappush(val)
        else:
            raise IndexError('Queue is already at maximum length, cannot put another element.')

    def get(self):
    # get should remove and return the root element of the heap (heappop)
    # raise an IndexError if called on an empty priority queue
        if len(self)>0:
            minheap = P2.MinHeap(self.elements)
            min_elem = minheap.heappop()
            return(min_elem)
        else:
            raise IndexError('Queue is empty, cannot perform get on an empty queue.')
            
    def peek(self):
    # peek should return the smallest value in the queue.
    # raise an IndexError if called on an empty priority queue
        if len(self)>0:
            minheap = P2.MinHeap(self.elements)
            min_elem = minheap.heappop()
            minheap.heappush(min_elem)
            return(min_elem)
        else:
            raise IndexError('Queue is empty, cannot perform peek from an empty queue.')
            
class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        PriorityQueue.__init__(self, max_size)
        
    def put(self, val):
    # put should push the element to the heap (heappush)
    # raise an IndexError if called after max_size is reached. Nothing should be returned
        if len(self)<self.max_size:
            heapq.heapify(self.elements)
            heapq.heappush(self.elements, val)
        else:
            raise IndexError('Queue is already at maximum length, cannot put another element.')

    def get(self):
    # get should remove and return the root element of the heap (heappop)
    # raise an IndexError if called on an empty priority queue
        if len(self)>0:
            return(heapq.heappop(self.elements))
        else:
            raise IndexError('Queue is empty, cannot perform get on an empty queue.')
            
    def peek(self):
    # peek should return the smallest value in the queue.
    # raise an IndexError if called on an empty priority queue
        if len(self)>0:
            min_elem = heapq.heappop(self.elements)
            heapq.heappush(self.elements,min_elem)
            return(min_elem)
        else:
            raise IndexError('Queue is empty, cannot perform peek from an empty queue.')
        
def generatelists(n, length=20, dictionary_path='./words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed

