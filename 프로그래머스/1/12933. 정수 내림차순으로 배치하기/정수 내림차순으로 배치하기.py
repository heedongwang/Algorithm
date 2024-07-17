def solution(n):
    li=[]

    for i in str(n):
        li.append(i)
    li.sort(reverse=True)
    str1= "".join(li)
    return int(str1)