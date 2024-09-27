
def GCD(n,m):
    while(m>0):
        n,m=m,n%m
    return n

def LCM(n,m):
    result=(n*m)//GCD(n,m)
    return result



def solution(n, m):
    answer = []
    answer=[GCD(n,m),LCM(n,m)]
    return answer
    