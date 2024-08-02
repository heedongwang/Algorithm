def solution(array, commands):
    answer = []
    for a,b,c, in commands:
        li=array[a-1:b]
        li.sort()
        answer.append(li[c-1])
    return answer
   