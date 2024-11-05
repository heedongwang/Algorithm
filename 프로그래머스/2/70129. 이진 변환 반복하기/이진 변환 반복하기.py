def solution(s):
    answer = []
    zero,roof=0,0
    while s!='1':
        zero += s.count('0')
        s = bin(s.count('1'))[2:]
        roof+=1
    answer=[roof,zero]
        
        
    return answer