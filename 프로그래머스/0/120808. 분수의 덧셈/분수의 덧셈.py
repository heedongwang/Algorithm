def gcd(a,b):
    if a%b==0: 
        return b
    return gcd(b, a%b)

def solution(numer1, denom1, numer2, denom2):
    answer = []

    a=gcd(numer1,numer2)
    num=(denom1*numer2+denom2*numer1)
    dem= denom1*denom2
    g= gcd(dem,num)
    answer.append(num//g)
    answer.append(dem//g)
    return answer