def solution(quiz):
    answer = []
    for i in quiz:
        eql,an= i.split("=")
        if eval(eql)==int(an):
            answer.append("O")
        else:
            answer.append("X")
        
        print(answer)
    return answer