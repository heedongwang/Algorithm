def solution(s):
    check=[]
    for i in s:
        if not check:
            check.append(i)
            continue
            
        last=check[-1]
        
        if last==i:
            check.pop()
        else:
            check.append(i)
        
    if not check:
        return 1

    return 0
