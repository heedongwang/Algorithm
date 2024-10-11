#큐
import sys
que=[]

def push(x):
    return que.append(x)

def pop():
    if empty()!=1:
        n=que[0]
        del que[0]
        return n
    else:
        return -1

def size():
    return len(que)

def empty():
    if  len(que)==0:
        return 1
    else:
        return 0

def front():
    if len(que)!=0:
        return que[0]
    else:
        return -1

def back():
    if  len(que)!=0:
        return que[-1]
    else:
        return -1
    
num=int(sys.stdin.readline())
for i in range(num):
    func =sys.stdin.readline().rstrip()
    if " "in func:
        f,x=func.split()
        push(int(x))
    elif func =="pop":
        print(pop())
    elif func== 'front':
        print(front())
    elif func=='back':
        print(back())
    elif func=="size":
        print(size())
    elif func =='empty':
        print(empty())
    

