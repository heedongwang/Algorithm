from collections import deque
def solution(prices):
    answer = []
    deq=deque(prices)
    
    while deq:
        stock=deq.popleft()
        cnt=0
        for i in deq:
                if stock <= i:
                    cnt += 1
                else:
                    cnt += 1
                    break
        answer.append(cnt)
    return answer