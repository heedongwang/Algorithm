def solution(quiz):
    answer = []
    li=[]
    for i in quiz:
        li= i.split("=")
        if eval(li[0])==int(li[1]):
            answer.append("O")
        else:
            answer.append("X")
        
        print(answer)
    return answer