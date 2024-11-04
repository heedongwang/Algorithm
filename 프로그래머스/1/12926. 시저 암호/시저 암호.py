#65~90: A~Z, 97~122:a~z


def solution(s, n):
    answer = ''
    li1=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    li2=list('abcdefghijklmnopqrstuvwxyz')

    for i in s:
        if i in li1:
            idx=li1.index(i)+n
            print(idx,end=" ")
            if idx>25:
                idx-=26
            answer+=li1[idx]
        elif i in li2:
            idx=li2.index(i)+n
            if idx>25:
                idx-=26
            print(idx, end=" ")
            answer+=li2[idx]
        else: answer+=" "

    return answer