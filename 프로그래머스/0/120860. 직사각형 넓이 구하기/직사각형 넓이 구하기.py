def solution(dots):
    li=sorted(dots)
    h=abs(li[0][0]-li[2][0])
    w=abs(li[0][1]-li[1][1])
    return h*w