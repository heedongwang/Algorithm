def solution(n):
    l=[True for _ in range(n+1)]
    l[1]=False
    for i in range(2,int(n**0.5)+1):
        if l[i]==True:
            j=2
            while i*j<=n:
                l[i*j]=False
                j+=1
            
    
    return l.count(True)-1