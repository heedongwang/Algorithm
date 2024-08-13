def solution(x):
    answer = True
    sum=0
    li=list(str(x))
    for i in li:
        sum+=int(i)
    if x%sum!=0:
        answer=False
    return answer