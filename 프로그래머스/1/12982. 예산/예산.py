def solution(d, budget):
    total=0
    a=[]
    d.sort()
    for i in d:
        if total<budget:
            a.append(i)
            total+=i
            if total-budget>0:
                del a[-1]         


    return len(a)