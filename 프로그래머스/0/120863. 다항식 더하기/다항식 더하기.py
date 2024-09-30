def solution(polynomial):
    answer = ''
    li=list(polynomial.split(" + "))
    xli,numli=[],[]
    for i in li:
        if i.isdigit():
            numli.append(i)
        else:
            xli.append(i)
            
    xsum,numsum=0,0
    
    for i in xli:
        if i.isalpha():
            xsum += 1 
        else:
            xsum+=int(i[:-1])
            
    for i in numli:
        numsum+=int(i)
    print(xsum,numsum)
    
    if xsum==1:
        if numsum==0:
            answer=f'x'
        elif xsum==0:
            answer=f'{numsum}'
        else:
            answer=f'x + {numsum}'
    else:
        if numsum==0:
            answer=f'{xsum}x'
        elif xsum==0:
            answer=f'{numsum}'
        else:
            answer=f'{xsum}x + {numsum}'


    return answer