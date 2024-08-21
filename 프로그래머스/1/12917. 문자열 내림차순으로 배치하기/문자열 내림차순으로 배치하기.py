def solution(s):
    answer = ''
    li=list(s)
    for i in range(len(li)):
        li[i]=ord(li[i])

    li.sort(reverse=True)

    for i in range(len(li)):
        li[i]=chr(li[i])

    return "".join(li)


    