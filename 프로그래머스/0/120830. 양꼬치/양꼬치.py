def solution(n, k):
    answer = 0
    if n>=10:
        sheep=n*12000
        if k>=(n//10):
            drink=(k-(n//10))*2000
    else:
        sheep=n*12000
        drink=k*2000
    answer=sheep+drink
    return answer