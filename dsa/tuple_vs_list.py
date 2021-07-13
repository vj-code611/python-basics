# tuple_vs_list

import sys
import timeit
print('test 1: size while saving:')

myList  = [0, 1, 3.3,  True, "Hello"]
myTuple = (0, 1, 3.3,  True, "Hello")

print(sys.getsizeof(myList), "bytes")  #120 bytes
print(sys.getsizeof(myTuple), "bytes") # 80 bytes


print('test 2: time while creating')
print(timeit.timeit(stmt="[0, 1, 3, 4, 5]", number=100000))  #0.010654914000000001 sec
print(timeit.timeit(stmt="(0, 1, 3, 4, 5)", number=100000))  #0.0021505440000000042 sec