def solution(t, p):
    num=""
    lit=list(t)
    li=[]
    count=0

    for j in range(len(lit)-len(p)+1):
        for k in range(len(p)):
            num+=lit[k+j]
        li.append(num)
        num=""
    li=list(map(int,li))
    for i in li:
        if int(p)>=i:
            count+=1
        

    return count