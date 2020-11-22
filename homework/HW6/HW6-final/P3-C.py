#/usr/bin/env python3

import P3
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size':14})

elapsed_NaivePriorityQueue = P3.timeit(pqclass=P3.NaivePriorityQueue)
elapsed_HeapPriorityQueue = P3.timeit(pqclass=P3.HeapPriorityQueue)
elapsed_PythonHeapPriorityQueue = P3.timeit(pqclass=P3.PythonHeapPriorityQueue)

elapsed_times = [elapsed_NaivePriorityQueue,elapsed_HeapPriorityQueue,elapsed_PythonHeapPriorityQueue]
names = ['Naive','Heap','Python Heap']
ns=[10, 20, 50, 100, 200, 500]

plt.figure(figsize=[7,7])

for elapsed_time, name in zip(elapsed_times,names):
    plt.plot(ns,elapsed_time,label=name)
    
plt.legend()
plt.xlabel('Number of Lists')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Efficiency of Heap Implementations')
plt.savefig('P3-C.png')
plt.show()
