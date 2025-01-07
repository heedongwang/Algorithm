def solution(s):
    answer = ''
    num=0
    for i in s:
        if i==" ":
            answer+=" "
            num=0
            continue
        num+=1
        if num%2!=0:
            answer+=i.upper()
        else:
            answer+=i.lower()
    return answer