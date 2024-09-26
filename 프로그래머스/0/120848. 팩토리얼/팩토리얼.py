import math
def solution(n):
    num = 1
    while math.factorial(num)<=n:
            if n%math.factorial(num)>=0:
                answer=num
            num+=1
            
    return answer