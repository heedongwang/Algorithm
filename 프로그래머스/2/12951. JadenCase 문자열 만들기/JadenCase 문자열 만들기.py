def solution(s):
    answer=" "
    s.lower()
    li=s.split(" ")
    word=[]
    print(li)
    for i in li:
        if i== "":
            word.append(i)
        elif i.isalpha():
            word.append(i.capitalize())
        elif  i.isalnum():
            word.append(i.lower())

    return " ".join(word)