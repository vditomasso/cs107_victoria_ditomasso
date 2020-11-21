#!/usr/bin/env python3

from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    def heapify(self, idx: int) -> None:
        # If an index is smaller than its parent, then swap and evaluate the next index
        
        comp_idxes = [self.left(idx),self.right(idx)]
        
        for comp_idx in comp_idxes:
            try:
                if self.elements[idx] > self.elements[comp_idx]:
                    self.swap(idx, comp_idx)
                    self.heapify(self.left(idx))
            except IndexError:
                pass

    def build_heap(self) -> None:
        for idx in range(self.size//2, 0, -1):
            self.heapify(idx)
        
        
### Demo ###

h = Heap([-1,0,0,15,23,1,2,3]) # The heap tree will be built during initialization
print(h)
