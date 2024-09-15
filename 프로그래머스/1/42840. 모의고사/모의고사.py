def count(answers,li):
    count=0
    for i in range(len(answers)):
        if answers[i]==li[i]:
            count+=1
    return count

def solution(answers):
    answer = []
    la=len(answers)
    st1=[1,2,3,4,5]
    st2=[2,1,2,3,2,4,2,5]
    st3=[3,3,1,1,2,2,4,4,5,5]
    
    l1=st1*(la//5)+st1[:la%5]
    l2=st2*(la//8)+st2[:la%8]
    l3=st3*(la//10)+st3[:la%10]
    
    c1=count(answers,l1)
    c2=count(answers,l2)
    c3=count(answers,l3)
    li=[c1,c2,c3]
    
    for i in range(3):
        if max(li)<=li[i]:
            answer.append((i+1))

    return answer