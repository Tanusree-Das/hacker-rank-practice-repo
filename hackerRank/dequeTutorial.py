'''A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque
with approximately the same  performance in either direction.'''

'''TASK:- Perform append, pop, popleft and appendleft methods on an empty deque '''

'''Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.'''

from collections import deque

if __name__=="__main__":
    no_of_operation=int(input())
    d=deque()
    for o in range(no_of_operation):
        operation_name,*operation=input().split()
        eval("d."+operation_name+"("+str(*operation)+")")
    print(*d)
