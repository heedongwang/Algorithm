def solution(n):
    li=[]
    hanoi(n,1,3,2,li)
    return li

def hanoi(n,a,b,c,li):  
    if n==1:
        li.append([a,b])
        return
    hanoi(n-1,a,c,b,li)
    li.append([a,b])
    hanoi(n-1,c,b,a,li)
    

