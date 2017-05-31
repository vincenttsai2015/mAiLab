from __future__ import division
import random
import statistics
from time import *


# 1. Generate and print 5 numbers in random.
print [random.random() for x in range(5)]
    
# 2. Generate N numbers between -1 and 1 in random. Please also evaluate and print their mean and variance.
for N in [10, 100, 1000, 10000, 100000]:
    list = []
    for y in range(N):
        list.append(random.uniform(-1,1))
    average = statistics.mean(list)
    std_dev = statistics.stdev(list)
    print "Average = ", average
    print "Standard deviation = ", std_dev
    
#3. Evaluate the time needed for generating N numbers in random.
for N in [10, 100, 1000, 10000, 100000]:
    list = []
    begin = time()
    for y in range(N):
        list.append(random.uniform(-1,1))
    end = time() - begin
    print "Time needed for generate ", N, "random numbers: ", end
    average = statistics.mean(list)
    std_dev = statistics.stdev(list)
    print "Average = ", average
    print "Standard deviation = ", std_dev