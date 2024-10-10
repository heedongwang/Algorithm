#스택
import sys
stack=[]

def push(stack,x):
    stack.append(x)
    
            
def pop():
    if empty()==1:
        return -1
    else:
        p=stack[-1]
        del stack[-1]
        return p
    
def empty():
    if len(stack)==0:
        return 1
    else:
        return 0

def size():
    return len(stack)
      
def top():
    if empty()== 1:
        return -1
    else:
        return stack[-1]

num = int(sys.stdin.readline().rstrip())
for i in range(num):
    inputs=sys.stdin.readline().rstrip()
    if " " in inputs:
        func,x=inputs.split()
        push(stack,int(x))
    elif inputs=='size':
        print(size())
    elif inputs=='empty':
        print(empty())
    elif inputs=='top':
        print(top())
    elif inputs=='pop':
        print(pop())