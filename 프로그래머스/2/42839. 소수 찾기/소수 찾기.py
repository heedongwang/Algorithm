from itertools import permutations
def isprime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    result=set()
    li=list(numbers)
    for i in range(1,len(li)+1):
        for j in permutations(li,i):
            result.add(int("".join(j)))
    for i in result:
        if isprime(i)==True:
            answer+=1
    print(result)
    
    return answer