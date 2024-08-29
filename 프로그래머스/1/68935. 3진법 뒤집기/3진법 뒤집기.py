def solution(n):
    answer = 0
    num=''
    while n>0:
        n,b=divmod(n,3)
        num+=str(b)
        
    answer=int(num,3)
    
    return answer