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

    def __len__(self) -> int:
        return self.size

    def heapify(self, idx: int) -> None:
        comp_idxes = [self.left(idx),self.right(idx)]

        for comp_idx in comp_idxes:
            try:
                if self.compare(idx,comp_idx):
#                if self.elements[idx] > self.elements[comp_idx]:
                    self.swap(idx, comp_idx)
                    self.heapify(self.left(idx))
                    self.heapify(self.right(idx))
            except IndexError:
                pass

    def build_heap(self) -> None:
        for idx in range(self.size-1, -1, -1):
            self.heapify(idx)

    def heappush(self, key: int) -> None:
        # inserts a new element into the heap (while maintining its heap-property!)
        elements = self.elements
        elements.append(key)
        self.elements = elements
        self.size+= 1
        self.build_heap()

    def heappop(self) -> int:
        # this function should remove the heap's first element (min for min heap, max for max heap) and return it to the caller
        # Raise an IndexError when trying to pop from an empty heap
        if self.size != 0:
            elements = self.elements
            pop = elements[0]
            elements.remove(pop)
            self.elements = elements
            self.size -= 1
            self.build_heap()
            return pop
        else:
            raise IndexError("Cannot heappop from an empty heap")

class MinHeap(Heap):
    def __init__(self, array: List[int]):
        Heap.__init__(self,array)
    
    def compare(self,idx1,idx2):
        '''idx1: index of the parent
        idx2: index of the child'''
        return(self.elements[idx1]>self.elements[idx2])
        

class MaxHeap(Heap):
    def __init__(self, array: List[int]):
        Heap.__init__(self,array)
    
    def compare(self,idx1,idx2):
        '''idx1: index of the parent
        idx2: index of the child'''
        return(self.elements[idx1]<self.elements[idx2])
