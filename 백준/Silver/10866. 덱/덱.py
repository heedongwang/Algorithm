#덱
import sys
from collections import deque
deque=deque()

def push_front(x):
    return deque.appendleft(x)

def push_back(x):
    return deque.append(x)

def pop_front():
    if empty()==1:
        return -1
    else:
        return deque.popleft()

def pop_back():
    if empty()==1:
        return -1
    else:
        return deque.pop()

def size():
    return len(deque)

def empty():
    if size()==0:
        return 1
    else:
        return 0

def front():
    if empty()==1:
        return -1
    else:
        return deque[0]

def back():
    if empty()==1:
        return -1
    else:
        return deque[-1]
    
    
num=int(sys.stdin.readline())
for i in range(num):
    f=sys.stdin.readline().rstrip()
    if " " in f:
        func,x= f.split()
        if func=='push_front':
            push_front(x)
        else:
            push_back(x)
    elif f=='pop_front':
        print(pop_front())
    elif f=='pop_back':
        print(pop_back())
    elif f== 'size':
        print(size())
    elif f== 'empty':
        print(empty())
    elif f=='front':
        print(front())
    elif f=='back':
        print(back())
        
