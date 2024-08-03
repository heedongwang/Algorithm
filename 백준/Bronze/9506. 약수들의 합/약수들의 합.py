while True:
    
    n=int(input())
    
    if n==-1:
        break
    
    li=list(filter(lambda x: n%x==0, range(1,n+1)))
    sums=sum(li)-n
    pr=[str(n),'=']

    if sums== n:
        for i in range(len(li)-1):
            pr.append(str(li[i]))
            pr.append('+')
        pr1=pr[:-1]
        print(' '.join(pr1))
    else:
        print(f"{n} is NOT perfect.")