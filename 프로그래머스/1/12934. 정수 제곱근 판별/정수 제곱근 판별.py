import math
def solution(n):
    answer = 0
    n1=math.sqrt(n)
    if int(n1)==n1:
        answer=(n1+1)**2
    else:
        answer=-1
    return answer