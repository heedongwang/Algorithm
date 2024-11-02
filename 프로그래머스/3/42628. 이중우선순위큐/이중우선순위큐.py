def solution(operations):
    answer = []
    for i in operations:
        if 'D 1'==i and len(answer)!=0:
            answer.remove(max(answer))
        elif 'D -1' ==i and len(answer)!=0:
            answer.remove(min(answer))
        elif "I" in i:
            oper,num=i.split()
            answer.append(int(num))

    if len(answer)>0:
        return [max(answer),min(answer)]
    else:
        return [0,0]