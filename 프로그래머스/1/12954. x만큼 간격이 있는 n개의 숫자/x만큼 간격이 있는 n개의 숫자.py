def solution(x, n):
    answer = []
    start=x
    end=(x*n)
    if x==0:
        answer=[0]*n
    elif x>0:
        for i in range(start,end+1,x):
            answer.append(i)
    elif x<0:
        for i in range(start,end-1,x):
            answer.append(i)

    return answer