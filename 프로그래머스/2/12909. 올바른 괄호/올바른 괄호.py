def solution(s):
    answer = True
    li=list(s)
    check=[]
    for i in range(len(li)):
        if li[i]=='(':
            check.append('(')
        else:
            if len(check)>=1:
                if check[-1]=='(' and li[i]==')':
                    check.pop()
                else:
                    return False
            else:
                return False
        
    if check:
        return False


    return True