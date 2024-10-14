from collections import deque
num=int(input())
deque=deque(i for i in range(1,num+1))
while True:
    if len(deque)>1:
        deque.popleft()
        deque.append(deque.popleft())
    if len(deque)==1:
        break
print(deque[0])