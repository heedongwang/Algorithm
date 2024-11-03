from collections import deque

def solution(priorities, location):
    answer = 0
    queue=deque(enumerate(priorities))

    while queue:
        a,b=queue.popleft()
        if any(b<p for _, p in queue):
                queue.append((a,b))
                print(queue)
        else:
            answer+=1
            if a==location:
                break
        
    return answer