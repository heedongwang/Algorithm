def solution(code):
    li=list(code)
    ret=[]
    mode=0
    for i in range(len(code)):
        if code[i]=='1':
            if mode==0:
                mode=1
            elif mode==1:
                mode=0
            
        if mode==1 and i%2==1 and code[i]!='1':
            ret.append(code[i])
        elif mode==0 and i%2==0 and code[i]!='1':
            ret.append(code[i])
    
    if len(ret)==0:
        return "EMPTY"
    else:
        return "".join(ret)